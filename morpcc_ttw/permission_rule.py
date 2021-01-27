import rulez
from morpcc.permission_rule import resolve_model_permission

from .app import App
from .entitycontent.model import (
    EntityContentCollection,
    EntityContentCollectionUI,
    EntityContentModel,
    EntityContentModelUI,
)


@App.permission_resolver(under=resolve_model_permission)
def resolve(request, model, permission, identity):
    usercol = request.get_collection("morpfw.pas.user")
    user = usercol.get_by_userid(identity.userid)
    opcol = request.get_collection("morpcc.objectpermissionassignment")

    epcol = request.get_collection("morpcc.entitypermissionassignment")

    permission_name = "%s:%s" % (permission.__module__, permission.__name__,)
    groups = user.groups()

    user_roles = []
    for gid, roles in user.group_roles().items():
        for role in roles:
            role_ref = "%s::%s" % (gid, role)
            user_roles.append(role_ref)

    # find entity model permission
    if isinstance(model, EntityContentModel) or isinstance(model, EntityContentModelUI):
        found_perms = []
        if isinstance(model, EntityContentModel):
            ec = model.collection
        elif isinstance(model, EntityContentModelUI):
            ec = model.model.collection
        else:
            # shouldnt reach here, but assert if hit
            raise AssertionError("Invalid model type")
        ecapp = ec.application()
        ecent = ec.entity()
        for perm in epcol.search(
            rulez.and_(
                rulez.field["application_uuid"] == ecapp.uuid,
                rulez.field["entity_uuid"] == ecent.uuid,
                rulez.field["permission"] == permission_name,
                rulez.field["enabled"] == True,
            )
        ):
            found_perms.append(perm)

        for perm in sorted(
            found_perms, key=lambda x: 0 if x["rule"] == "reject" else 1
        ):
            for role in user_roles:
                if role in (perm["roles"] or []):
                    if perm["rule"] == "allow":
                        return True
                    return False

    # find entity collection permission
    if isinstance(model, EntityContentCollection) or isinstance(
        model, EntityContentCollectionUI
    ):
        found_perms = []
        if isinstance(model, EntityContentCollection):
            ec = model
        elif isinstance(model, EntityContentCollectionUI):
            ec = model.collection
        else:
            # shouldnt reach here, but assert if hit
            raise AssertionError("Invalid model type")
        ecapp = ec.application()
        ecent = ec.entity()
        for perm in epcol.search(
            rulez.and_(
                rulez.field["application_uuid"] == ecapp.uuid,
                rulez.field["entity_uuid"] == ecent.uuid,
                rulez.field["permission"] == permission_name,
                rulez.field["enabled"] == True,
            )
        ):
            found_perms.append(perm)

        for perm in sorted(
            found_perms, key=lambda x: 0 if x["rule"] == "reject" else 1
        ):
            for role in user_roles:
                if role in (perm["roles"] or []):
                    if perm["rule"] == "allow":
                        return True
                    return False

    # find application permission
    if (
        isinstance(model, EntityContentCollection)
        or isinstance(model, EntityContentCollectionUI)
        or isinstance(model, EntityContentModel)
        or isinstance(model, EntityContentModelUI)
    ):
        found_perms = []
        if isinstance(model, EntityContentCollection):
            ec = model
        elif isinstance(model, EntityContentCollectionUI):
            ec = model.collection
        elif isinstance(model, EntityContentModel):
            ec = model.collection
        elif isinstance(model, EntityContentModelUI):
            ec = model.model.collection
        else:
            # shouldnt reach here, but assert if hit
            raise AssertionError("Invalid model type")
        ecapp = ec.application()
        ecent = ec.entity()
        for perm in opcol.search(
            rulez.and_(
                rulez.field["object_uuid"] == ecapp.uuid,
                rulez.field["permission"] == permission_name,
                rulez.field["enabled"] == True,
            )
        ):
            found_perms.append(perm)

        for perm in sorted(
            found_perms, key=lambda x: 0 if x["rule"] == "reject" else 1
        ):
            for role in user_roles:
                if role in (perm["roles"] or []):
                    if perm["rule"] == "allow":
                        return True
                    return False

