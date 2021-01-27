from morpfw.static import StaticRoot as BaseStaticRoot
from .app import App


class StaticRoot(BaseStaticRoot):

    module = 'morpcc_ttw'
    directory = 'static_files'


@App.path(model=StaticRoot, path='/__static__/morpcc_ttw', absorb=True)
def get_staticroot(absorb):
    return StaticRoot(absorb)

