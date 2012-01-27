from annoying.decorators import render_to


@render_to("viewer/home.html")
def test(request):
    return locals()
