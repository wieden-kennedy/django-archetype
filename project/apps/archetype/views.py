from annoying.decorators import render_to


@render_to("archetype/test.html")
def test(request):
    return locals()
