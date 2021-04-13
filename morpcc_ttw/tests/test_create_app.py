import os

import morpfw
import morpfw.sql
import pytest
from morpcc_ttw.app import App as TTWApp
from morpfw.cli.cli import load_settings

from ..application.adapters import ApplicationDatabaseSyncAdapter
from ..navigator import Navigator
from .scripts.create_app import create_app
from .scripts.import_metadata import import_metadata


class App(TTWApp):
    pass


@pytest.mark.filterwarnings("")
def test_create_app(pgsql_db, pgsql_db_warehouse):
    # FIXME: currently only testing that script run without failure
    # need to assert on whether records are created correctly or not
    settings = load_settings(
        os.path.join(os.path.dirname(__file__), "test_create_app-settings.yml")
    )
    with morpfw.request_factory(settings=settings) as request:
        morpfw.sql.Base.metadata.create_all(bind=request.db_session.bind)

    # import data dictionary
    with morpfw.request_factory(settings=settings) as request:
        import_metadata(request)

    # create app
    with morpfw.request_factory(settings=settings) as request:
        app_uuid = create_app(request).uuid

    # initialize warehouse
    with morpfw.request_factory(settings=settings) as request:
        app = request.get_collection("morpcc.application").get(app_uuid)
        dbsync = ApplicationDatabaseSyncAdapter(app, request)
        dbsync.update()

