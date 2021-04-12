import typing
from dataclasses import dataclass, field

import morpfw
from morpcc.deform.codewidget import CodeWidget
from morpcc.deform.richtextwidget import RichTextWidget
from morpcc.preparer.html import HTMLSanitizer
from morpfw.validator.field import valid_namespaced_identifier


@dataclass
class EndpointSchema(morpfw.Schema):

    name: typing.Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "editable": False,
            "validators": [valid_namespaced_identifier],
        },
    )

    title: typing.Optional[str] = field(default=None, metadata={"required": True})
    description: typing.Optional[str] = field(default=None, metadata={"format": "text"})
    notes: typing.Optional[str] = field(
        default=None,
        metadata={
            "format": "text/html",
            "preparers": [HTMLSanitizer()],
            "deform.widget": RichTextWidget(),
        },
    )

    __unique_constraint__ = ["name"]
