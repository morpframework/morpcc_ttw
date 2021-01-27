import morpfw
from morpfw.authz.pas import DefaultAuthzPolicy
from morpfw.crud import permission as crudperm

# 
import morpcc
import morpcc.permission as ccperm

# 

# 


class AppRoot(morpcc.Root):
    """ Application root for morpcc_ttw"""

    pass


class App(morpcc.App):
    """ morpcc_ttw Application """

    pass


@App.path(model=AppRoot, path="/")
def get_approot(request):
    return AppRoot(request)


@App.template_directory()
def get_template_directory():
    return "templates"


# 
