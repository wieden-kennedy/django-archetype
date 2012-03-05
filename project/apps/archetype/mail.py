import re
from BeautifulSoup import BeautifulSoup
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib.staticfiles.finders import find
from email.MIMEBase import MIMEBase
from django.core.mail import SafeMIMEMultipart


def image_finder(tag):
    return (tag.name == u'img' or
        tag.name == u'table' and 'background' in tag)


class EmailMultiPartWithEmbeddedImages(EmailMultiAlternatives):
    """
    A subclass of EmailMessage that allows text and html multipart content,
    automatically adding any images included in the templates.
    """
    alternative_subtype = 'alternative'

    related_subtype = 'related'

    def __init__(self, subject='', text_content='', html_content='', from_email=None, to=None, bcc=None,
            connection=None, attachments=None, headers=None, alternatives=None):
        # self.related_ids = []
        self.related_attachments = []
        super(EmailMultiPartWithEmbeddedImages, self).__init__(subject, text_content, from_email, to, bcc, connection, attachments, headers, alternatives)
        html_content_with_images = self.html_with_inline_images(html_content)
        self.attach_alternative(html_content_with_images, 'text/html')

    def attach_related(self, filename=None, content=None, mimetype=None):
        """
        Attaches a file with the given filename and content. The filename can
        be omitted and the mimetype is guessed, if not provided.

        If the first parameter is a MIMEBase subclass it is inserted directly
        into the resulting message attachments.
        """
        if isinstance(filename, MIMEBase):
            assert content == mimetype == None
            self.related_attachments.append(filename)
        else:
            assert content is not None
            self.related_attachments.append((filename, content, mimetype))

    def attach_related_file(self, path, mimetype=None):
        """Attaches a file from the filesystem."""
        content = open(find(path), 'rb').read()
        self.attach_related(path, content, mimetype)

    def _create_message(self, msg):
        return self._create_attachments(self._create_related_attachments(self._create_alternatives(msg)))

    def _create_alternatives(self, msg):
        for i, (content, mimetype) in enumerate(self.alternatives):
            if mimetype == 'text/html':
                for filename, _, _ in self.related_attachments:
                    content = re.sub(r'(?<!cid:)%s' % re.escape(filename), 'cid:%s' % filename, content)
                    content = re.sub(settings.STATIC_URL, '', content)
                self.alternatives[i] = (content, mimetype)

        return super(EmailMultiPartWithEmbeddedImages, self)._create_alternatives(msg)

    def _create_related_attachments(self, msg):
        encoding = self.encoding or settings.DEFAULT_CHARSET
        if self.related_attachments:
            body_msg = msg
            msg = SafeMIMEMultipart(_subtype=self.related_subtype, encoding=encoding)
            if self.body:
                msg.attach(body_msg)
            for related in self.related_attachments:
                msg.attach(self._create_related_attachment(*related))
        return msg

    def _create_related_attachment(self, filename, content, mimetype=None):
        """
        Convert the filename, content, mimetype triple into a MIME attachment
        object. Adjust headers to use Content-ID where applicable.
        Taken from http://code.djangoproject.com/ticket/4771
        """
        attachment = super(EmailMultiPartWithEmbeddedImages, self)._create_attachment(filename, content, mimetype)
        if filename:
            mimetype = attachment['Content-Type']
            del(attachment['Content-Type'])
            del(attachment['Content-Disposition'])
            attachment.add_header('Content-Disposition', 'inline', filename=filename)
            attachment.add_header('Content-Type', mimetype, name=filename)
            attachment.add_header('Content-ID', '<%s>' % filename)
        return attachment

    def html_with_inline_images(self, html_content):
        # parse self.html_content
        soup = BeautifulSoup(html_content)
        images = []
        added_images = []

        # Image processing, replace the current image urls with attached images.
        for index, tag in enumerate(soup.findAll(image_finder)):
            if tag.name == u'img':
                name = 'src'
            elif tag.name == u'table':
                name = 'background'
            # If the image was already added, skip it.
            if tag[name] in added_images:
                continue
            added_images.append(tag[name])
            images.append((tag[name], 'img%d@wk.com' % index))
        html_content = str(soup)

        # attach the images, update the html
        for filename, file_id in images:
            full_filename = filename.replace(settings.STATIC_URL, "")
            self.attach_related_file(full_filename)

        return html_content


class EmailMultiPartWithLinkedImages(EmailMultiAlternatives):
    """
    A subclass of EmailMessage that allows text and html multipart content,
    automatically adding any images included in the templates.
    """
    related_subtype = 'related'

    def __init__(self, subject='', text_content='', html_content='', from_email=None, to=None, bcc=None,
            connection=None, attachments=None, headers=None, alternatives=None):
        # self.related_ids = []
        self.related_attachments = []
        super(EmailMultiPartWithLinkedImages, self).__init__(subject, text_content, from_email, to, bcc, connection, attachments, headers, alternatives)

        self.attach_alternative(html_content, 'text/html')
