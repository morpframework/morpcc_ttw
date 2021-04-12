from ..app import App
from .model import EndpointHandlerCollection, EndpointHandlerModel

#
from .modelui import EndpointHandlerCollectionUI, EndpointHandlerModelUI

#
from .storage import EndpointHandlerStorage


def get_collection(request):
    storage = EndpointHandlerStorage(request)
    return EndpointHandlerCollection(request, storage)


def get_model(request, identifier):
    col = get_collection(request)
    return col.get(identifier)


@App.path(model=EndpointHandlerCollection, path="/api/ttw.endpointhandler")
def _get_collection(request):
    return get_collection(request)


@App.path(model=EndpointHandlerModel, path="/api/ttw.endpointhandler/{identifier}")
def _get_model(request, identifier):
    return get_model(request, identifier)


#


@App.path(model=EndpointHandlerCollectionUI, path="/ttw.endpointhandler")
def _get_collection_ui(request):
    collection = get_collection(request)
    return collection.ui()


@App.path(model=EndpointHandlerModelUI, path="/ttw.endpointhandler/{identifier}")
def _get_model_ui(request, identifier):
    model = get_model(request, identifier)
    if model:
        return model.ui()


#

