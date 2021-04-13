import morpfw

from .app import App
from .entitycontent.model import (
    EntityContentCollection,
    EntityContentModel,
    content_collection_factory,
)


class EntityContentCollectionMetalinkProvider(morpfw.MetalinkProvider):
    def link(self, obj, view_name=None, **kwargs) -> dict:
        raise NotImplementedError

    def resolve(self, link) -> str:
        raise NotImplementedError


class EntityContentModelMetalinkProvider(morpfw.MetalinkProvider):
    def link(self, obj: EntityContentModel, view_name=None, **kwargs) -> dict:
        return {
            "type": "morpcc_ttw.entitycontentmodel",
            "application_uuid": obj.application().uuid,
            "entity_uuid": obj.entity().uuid,
            "uuid": obj.uuid,
            "view_name": view_name,
        }

    def resolve(self, link) -> str:
        request = self.request
        app_col = request.get_collection("morpcc.application")
        entity_col = request.get_collection("morpcc.entity")
        app = app_col.get(link["application_uuid"])
        entity = entity_col.get(link["entity_uuid"])
        content_col = content_collection_factory(entity, app)
        obj = content_col.get(link["uuid"])
        if link["view_name"]:
            return request.link(obj, link["view_name"])
        return request.link(obj)


@App.metalink(name="morpcc_ttw.entitycontentcollection", model=EntityContentCollection)
def get_ecc_metalink(request):
    return EntityContentCollectionMetalinkProvider(request)


@App.metalink(name="morpcc_ttw.entitycontentmodel", model=EntityContentModel)
def get_ecm_metalink(request):
    return EntityContentModelMetalinkProvider(request)
