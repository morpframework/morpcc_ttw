from ..app import App
from .model import EntityValidatorCollection, EntityValidatorModel

#
from .modelui import EntityValidatorCollectionUI, EntityValidatorModelUI

#
from .storage import EntityValidatorStorage


def get_collection(request):
    storage = EntityValidatorStorage(request)
    return EntityValidatorCollection(request, storage)


def get_model(request, identifier):
    col = get_collection(request)
    return col.get(identifier)


@App.path(model=EntityValidatorCollection, path="/api/ttw.entityvalidator")
def _get_collection(request):
    return get_collection(request)


@App.path(model=EntityValidatorModel, path="/api/ttw.entityvalidator/{identifier}")
def _get_model(request, identifier):
    return get_model(request, identifier)


#


@App.path(model=EntityValidatorCollectionUI, path="/ttw.entityvalidator")
def _get_collection_ui(request):
    collection = get_collection(request)
    if collection:
        return collection.ui()


@App.path(model=EntityValidatorModelUI, path="/ttw.entityvalidator/{identifier}")
def _get_model_ui(request, identifier):
    model = get_model(request, identifier)
    if model:
        return model.ui()


#
