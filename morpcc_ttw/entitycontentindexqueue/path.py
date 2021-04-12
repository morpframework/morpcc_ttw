from ..app import App
from .model import EntityContentIndexQueueCollection, EntityContentIndexQueueModel

#
from .modelui import EntityContentIndexQueueCollectionUI, EntityContentIndexQueueModelUI

#
from .storage import EntityContentIndexQueueStorage


def get_collection(request):
    storage = EntityContentIndexQueueStorage(request)
    return EntityContentIndexQueueCollection(request, storage)


def get_model(request, identifier):
    col = get_collection(request)
    return col.get(identifier)


@App.path(
    model=EntityContentIndexQueueCollection, path="/api/ttw.entitycontentindexqueue"
)
def _get_collection(request):
    return get_collection(request)


@App.path(
    model=EntityContentIndexQueueModel,
    path="/api/ttw.entitycontentindexqueue/{identifier}",
)
def _get_model(request, identifier):
    return get_model(request, identifier)


#


@App.path(
    model=EntityContentIndexQueueCollectionUI, path="/ttw.entitycontentindexqueue"
)
def _get_collection_ui(request):
    collection = get_collection(request)
    return collection.ui()


@App.path(
    model=EntityContentIndexQueueModelUI,
    path="/ttw.entitycontentindexqueue/{identifier}",
)
def _get_model_ui(request, identifier):
    model = get_model(request, identifier)
    if model:
        return model.ui()

#

