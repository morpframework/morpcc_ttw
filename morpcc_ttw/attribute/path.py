from ..app import App
from .model import AttributeCollection, AttributeModel

#
from .modelui import AttributeCollectionUI, AttributeModelUI

#
from .storage import AttributeStorage


def get_collection(request):
    storage = AttributeStorage(request)
    return AttributeCollection(request, storage)


def get_model(request, identifier):
    col = get_collection(request)
    return col.get(identifier)


@App.path(model=AttributeCollection, path="/api/ttw.attribute")
def _get_collection(request):
    return get_collection(request)


@App.path(model=AttributeModel, path="/api/ttw.attribute/{identifier}")
def _get_model(request, identifier):
    return get_model(request, identifier)


@App.path(model=AttributeCollectionUI, path="/ttw.attribute")
def _get_collection_ui(request):
    collection = get_collection(request)
    if collection:
        return collection.ui()


@App.path(model=AttributeModelUI, path="/ttw.attribute/{identifier}")
def _get_model_ui(request, identifier):
    model = get_model(request, identifier)
    if model:
        return model.ui()


#
