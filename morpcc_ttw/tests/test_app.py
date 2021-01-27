from morpcc.tests.democms_common import follow, get_democms_client


def test_app(pgsql_db, pgsql_db_warehouse, pgsql_db_cache):

    # test application creation
    c = get_democms_client()
    r = c.post(
        "/application/+create",
        {
            "__formid__": "deform",
            "name": "test_app",
            "title": "Application",
            "icon": "database",
        },
    )

    app_loc = r.headers["Location"]
    app_uuid = app_loc.split("/")[-1]

    assert r.headers.get("X-MORP-FORM-FAILED", None) is None
    assert r.status_code == 302
    assert follow(r).status_code == 200
    # create entity

    r = c.post(
        "/entity/+create",
        {
            "__formid__": "deform",
            "name": "person",
            "title": "Person",
            "application_uuid": app_uuid,
        },
    )

    assert r.headers.get("X-MORP-FORM-FAILED", None) is None
    assert r.status_code == 302
    person_loc = r.headers["Location"]
    person_uuid = person_loc.split("/")[-1]
    assert follow(r).status_code == 200

    # create attribute
    r = c.post(
        "/attribute/+create",
        {
            "__formid__": "deform",
            "name": "personid",
            "type": "integer",
            "title": "Person ID",
            "entity_uuid": person_uuid,
        },
    )

    assert r.headers.get("X-MORP-FORM-FAILED", None) is None
    assert r.status_code == 302

    person_id_loc = r.headers["Location"]
    person_id_uuid = person_id_loc.split("/")[-1]

    assert follow(r).status_code == 200

    r = c.post(
        "/attribute/+create",
        {
            "__formid__": "deform",
            "name": "full_name",
            "type": "string",
            "title": "Full Name",
            "entity_uuid": person_uuid,
        },
    )

    assert r.headers.get("X-MORP-FORM-FAILED", None) is None

    person_name_loc = r.headers["Location"]
    person_name_uuid = person_name_loc.split("/")[-1]

    assert r.status_code == 302
    assert follow(r).status_code == 200

    r = c.post(
        "/behaviorassignment/+create",
        {
            "__formid__": "deform",
            "behavior": "morpcc.titled_document",
            "entity_uuid": person_uuid,
        },
    )

    assert r.headers.get("X-MORP-FORM-FAILED", None) is None
    assert r.status_code == 302
    assert follow(r).status_code == 200

    r = c.post(
        "/entity/+create",
        {
            "__formid__": "deform",
            "name": "address",
            "title": "Address",
            "application_uuid": app_uuid,
        },
    )

    assert r.headers.get("X-MORP-FORM-FAILED", None) is None
    address_loc = r.headers.get("Location")
    address_uuid = address_loc.split("/")[-1]

    assert r.status_code == 302
    assert follow(r).status_code == 200

    r = c.post(
        "/attribute/+create",
        {
            "__formid__": "deform",
            "name": "address",
            "type": "string",
            "title": "Address",
            "entity_uuid": address_uuid,
        },
    )

    assert r.headers.get("X-MORP-FORM-FAILED", None) is None
    assert r.status_code == 302
    assert follow(r).status_code == 200

    r = c.post(
        "/relationship/+create",
        {
            "__formid__": "deform",
            "name": "personid",
            "title": "Person",
            "entity_uuid": address_uuid,
            "reference_attribute_uuid": person_id_uuid,
            "reference_search_attribute_uuid": person_name_uuid,
        },
    )

    assert r.headers.get("X-MORP-FORM-FAILED", None) is None
    person_address_rel_loc = r.headers.get("Location")
    person_address_rel_uuid = person_address_rel_loc.split("/")[-1]
    assert r.status_code == 302
    assert follow(r).status_code == 200

    r = c.post(
        "/backrelationship/+create",
        {
            "__formid__": "deform",
            "name": "addresses",
            "title": "Addresses",
            "entity_uuid": address_uuid,
            "reference_relationship_uuid": person_address_rel_uuid,
        },
    )

    assert r.headers.get("X-MORP-FORM-FAILED", None) is None
    assert r.status_code == 302
    assert follow(r).status_code == 200
