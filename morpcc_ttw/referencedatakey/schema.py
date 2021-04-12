import typing
from dataclasses import dataclass, field

import morpfw
from morpcc.deform.referencewidget import ReferenceWidget
from morpcc.validator.field import valid_refdatakey
from morpcc.validator.reference import ReferenceValidator
from morpfw.validator.field import valid_identifier


@dataclass
class ReferenceDataKeySchema(morpfw.Schema):

    name: typing.Optional[str] = field(
        default=None,
        metadata={
            "editable": False,
            "validators": [valid_refdatakey],
            "required": True,
        },
    )
    description: typing.Optional[str] = field(default=None, metadata={"format": "text"})
    referencedata_uuid: typing.Optional[str] = field(
        default=None,
        metadata={
            "title": "Reference Data",
            "format": "uuid",
            "editable": False,
            "required": True,
            "validators": [ReferenceValidator("morpcc.referencedata", "uuid")],
            "deform.widget": ReferenceWidget("morpcc.referencedata", "title", "uuid"),
        },
    )

    __unique_constraint__ = ["name", "referencedata_uuid"]
