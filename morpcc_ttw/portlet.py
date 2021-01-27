from morpcc.portlet import types_navigation
from morpcc.util import permits, typeinfo_link
from morpfw.crud import permission as crudperms

from .app import App


@App.portlet(name="morpcc.main_navigation", template="master/portlet/navigation.pt")
def navigation_portlet(context, request):

    general_children = [
        {"title": "Home", "icon": "home", "href": request.relative_url("/")},
    ]

    appcol = request.get_collection("morpcc.application")
    apps_nav = []
    for app in appcol.all():
        appui = app.ui()
        if permits(request, appui, crudperms.View):
            apps_nav.append(
                {
                    "title": app["title"],
                    "icon": app["icon"] or "cubes",
                    "href": request.link(appui, "+{}".format(appui.default_view)),
                }
            )

    types_nav = types_navigation(request)

    navtree = []
    navtree.append({"section": "General", "children": general_children})
    if apps_nav:
        navtree.append({"section": "Applications", "children": apps_nav})
    if types_nav:
        navtree.append({"section": "Collections", "children": types_nav})

    return {"navtree": navtree}

