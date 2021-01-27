from morpfw.crud import permission as crudperm

from .app import App


@App.setting_modules(name="morpcc_ttw", title="Through-The-Web (TTW) Development")
def get_modules(request):
    modules = []
    if request.permits("/schema", crudperm.Search):
        modules.append(
            {
                "title": "Manage Schemas",
                "icon": "file-code-o",
                "href": request.relative_url("/schema/+listing"),
            }
        )

    if request.permits("/referencedata", crudperm.Search):
        modules.append(
            {
                "title": "Manage Reference Data",
                "icon": "book",
                "href": request.relative_url("/referencedata/+listing"),
            }
        )

    if request.permits("/attributevalidator", crudperm.Search):
        modules.append(
            {
                "title": "Manage Attribute Validators",
                "icon": "check-circle",
                "href": request.relative_url("/attributevalidator/+listing"),
            },
        )

    if request.permits("/entityvalidator", crudperm.Search):
        modules.append(
            {
                "title": "Manage Entity Validators",
                "icon": "check-square",
                "href": request.relative_url("/entityvalidator/+listing"),
            }
        )

    if request.permits("/dictionaryentity", crudperm.Search):
        modules.append(
            {
                "title": "Manage Data Dictionary",
                "icon": "book",
                "href": request.relative_url("/dictionaryentity/+listing"),
            }
        )

    if request.permits("/application", crudperm.Search):
        modules.append(
            {
                "title": "Manage Applications",
                "icon": "cubes",
                "href": request.relative_url("/application/+listing"),
            }
        )

    if request.permits("/endpoint", crudperm.Search):
        modules.append(
            {
                "title": "Manage API Endpoints",
                "icon": "code",
                "href": request.relative_url("/endpoint/+listing"),
            }
        )

    return modules
