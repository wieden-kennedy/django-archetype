from django.http import HttpResponse
from django.conf import settings

from annoying.decorators import render_to


@render_to("archetype/test.html")
def test(request):
    return locals()


def robots_txt(request, allow=True):
    try:
        if settings.ENV == "STAGING" or settings.ENV == "DEV":
            return HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")
    except:
        pass
    if allow:
        return HttpResponse("User-agent: *\nAllow: /", mimetype="text/plain")
    else:
        return HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")


def always_500(request):
    assert True == "This view passes"
    return locals()
