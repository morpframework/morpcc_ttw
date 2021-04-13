import json
import os

import transaction
import yaml
from morpcc_ttw.navigator import Navigator

here = os.path.dirname(__file__)


def import_metadata(request):
    request.environ["morpfw.nomemoize"] = True

    REFDATA = {}
    for rd in open(os.path.join(here, "refdata.json")):
        row = json.loads(rd)
        name = row["field"]
        REFDATA.setdefault(name, {"title": name.title(), "data": []})
        if row["code"].upper() not in [k["key"] for k in REFDATA[name]["data"]]:
            REFDATA[name]["data"].append(
                {"key": row["code"].upper(), "label": row["value"]}
            )

    DD = yaml.load(open(os.path.join(here, "datadict.yml")), Loader=yaml.Loader)

    apps = Navigator(request)

    # referencedata
    for rdname, rdconf in REFDATA.items():
        rd = apps.add_referencedata(rdname, rdconf["title"])
        for rdc in rdconf["data"]:
            rdkey = rd.add_key(name=rdc["key"])
            rdkey.add_property(name="label", value=rdc["label"])

    # datadictionary
    for dent, dentconf in DD.items():
        ddel = apps.add_dictionaryentity(dent, dentconf["title"])
        for ddname, ddconf in dentconf["elements"].items():
            ddel.add_element(name=ddname, **ddconf)

    # we group everything as "general" for now
    dd = apps.datadictionary["general"]

    return dd
