from annoying.decorators import render_to


@render_to("sample_app/home.html")
def home(request):
    return locals()
