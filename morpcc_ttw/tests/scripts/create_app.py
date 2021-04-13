from datetime import datetime

from morpcc_ttw.navigator import Navigator


def create_app(request):
    request.environ["morpfw.nomemoize"] = True

    now = datetime.now()
    nav = Navigator(request)

    dd = nav.datadictionary["general"]

    # Entity: CIFID

    schema = nav.add_schema(name="schema2", title="Customer MDM")
    # Entity: Profile

    profile = schema.add_entity(name="customer", title="Customer")

    profile.add_attribute(
        name="cifid",
        title="CIF ID",
        type_="string",
        required=True,
        dictionaryelement=dd["cifid"],
    )

    profile.add_attribute(
        name="full_name",
        title="Full Name",
        type_="string",
        dictionaryelement=dd["full_name"],
        required=True,
        allow_invalid=True,
    )
    profile.add_attribute(name="first_name", title="First Name", type_="string")
    profile.add_attribute(name="middle_name", title="Middle Name", type_="string")
    profile.add_attribute(name="last_name", title="Last Name", type_="string")
    profile.add_attribute(
        name="customer_status",
        title="Customer Status",
        type_="string",
        dictionaryelement=dd["customer_status"],
    )
    profile.add_attribute(
        name="date_of_birth",
        title="Date Of Birth",
        type_="date",
        dictionaryelement=dd["date_of_birth"],
        required=True,
        allow_invalid=True,
    )
    profile.add_attribute(
        name="gender",
        title="Gender",
        type_="string",
        dictionaryelement=dd["gender"],
        required=True,
        allow_invalid=True,
    )
    profile.add_attribute(
        name="registered_date",
        title="Registration Date",
        type_="datetime",
        required=True,
        allow_invalid=True,
    )
    profile.add_attribute(
        name="race",
        title="Race",
        type_="string",
        dictionaryelement=dd["race"],
        required=True,
        allow_invalid=True,
    )
    profile.add_attribute(
        name="email", title="Email", type_="string", dictionaryelement=dd["email"],
    )
    profile.add_attribute(name="employer_name", title="Employer Name", type_="string")
    profile.add_attribute(name="occupation", title="Occupation", type_="string")

    # Historical CIF IDs

    cifid = schema.add_entity(name="historical_cifid", title="CIF ID")
    cifid.add_attribute(
        name="cifid",
        title="CIF ID",
        type_="string",
        required=True,
        dictionaryelement=dd["cifid"],
    )
    cifid.add_relationship(
        name="latest_cifid",
        title="Latest CIF ID",
        reference_attribute=profile.attributes["cifid"],
        reference_search_attribute=profile.attributes["cifid"],
        required=True,
    )
    profile.add_backrelationship(
        name="cifids",
        title="CIF IDs",
        reference_relationship=cifid.relationships["latest_cifid"],
    )

    # Entity : ID Docs

    iddocs = schema.add_entity(
        name="identification_documents", title="Identification Documents"
    )
    iddocs.add_relationship(
        name="cifid",
        title="CIF ID",
        reference_attribute=profile.attributes["cifid"],
        reference_search_attribute=profile.attributes["cifid"],
        required=True,
    )
    profile.add_backrelationship(
        name="identification_documents",
        title="Identification Documents",
        reference_relationship=iddocs.relationships["cifid"],
    )

    iddocs.add_attribute(
        name="type",
        title="ID Document Type",
        type_="string",
        dictionaryelement=dd["id_doc_type"],
        required=True,
        allow_invalid=True,
    )
    iddocs.add_attribute(
        name="issue_date",
        title="Issued Date",
        type_="date",
        required=True,
        allow_invalid=True,
    )
    iddocs.add_attribute(name="expiry_date", title="Expiry Date", type_="date")
    iddocs.add_attribute(name="id_doc", title="ID Document", type_="string")
    iddocs.add_attribute(
        name="nationality",
        title="Nationality",
        type_="string",
        dictionaryelement=dd["countries"],
        allow_invalid=True,
    )

    # Entity: Address

    address = schema.add_entity(name="address", title="Address")
    address.add_relationship(
        name="cifid",
        title="CIF ID",
        reference_attribute=profile.attributes["cifid"],
        reference_search_attribute=profile.attributes["cifid"],
        required=True,
    )
    profile.add_backrelationship(
        name="addresses",
        title="Addresses",
        reference_relationship=address.relationships["cifid"],
    )

    address.add_attribute(name="address_line1", title="Line 1", type_="string")
    address.add_attribute(name="address_line2", title="Line 2", type_="string")
    address.add_attribute(name="postcode", title="Postcode", type_="string")
    address.add_attribute(
        name="country",
        title="Country",
        type_="string",
        dictionaryelement=dd["countries"],
        allow_invalid=True,
    )
    address.add_attribute(
        name="address_type",
        title="Address Type",
        type_="string",
        dictionaryelement=dd["address_types"],
    )

    # Entity: Phone

    phone = schema.add_entity(name="phone", title="Phone")
    phone.add_relationship(
        name="cifid",
        title="CIF ID",
        reference_attribute=profile.attributes["cifid"],
        reference_search_attribute=profile.attributes["cifid"],
    )
    profile.add_backrelationship(
        name="phones",
        title="Phones",
        reference_relationship=phone.relationships["cifid"],
    )

    phone.add_attribute(
        name="number",
        type_="string",
        title="Phone Number",
        required=True,
        allow_invalid=True,
    )
    phone.add_attribute(name="serial_no", type_="string", title="Serial Number")

    # Entity: Cross References

    crossref = schema.add_entity(name="lob_reference", title="LOB Reference")
    crossref.add_relationship(
        name="cifid",
        title="CIF ID",
        reference_attribute=profile.attributes["cifid"],
        reference_search_attribute=profile.attributes["cifid"],
    )
    profile.add_backrelationship(
        name="lob_references",
        title="LOB References",
        reference_relationship=crossref.relationships["cifid"],
    )

    crossref.add_attribute(name="system", type_="string", title="System", required=True)
    crossref.add_attribute(
        name="id_in_source", type_="string", title="ID In Source", required=True
    )

    app = nav.add_application(
        name="customermdm", title="Customer MDM", schema=schema.schema
    )

    return app.application

