from . models import Year


def menu_links(request):
    links=Year.objects.all()
    return dict(links=links)