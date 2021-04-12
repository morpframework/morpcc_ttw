import typing
from dataclasses import dataclass, field

import morpfw
from deform.widget import Select2Widget, TextAreaWidget
from morpcc.deform.codewidget import CodeWidget
from morpcc.deform.referencewidget import ReferenceWidget
from morpcc.deform.richtextwidget import RichTextWidget
from morpcc.deform.vocabularywidget import VocabularyWidget
from morpcc.preparer.html import HTMLSanitizer
from morpcc.validator.reference import ReferenceValidator
from morpcc.validator.vocabulary import VocabularyValidator
from morpfw.validator.field import valid_namespaced_identifier

from ..attribute.schema import ACCEPTED_TYPES, valid_type


@dataclass
class AttributeValidatorSchema(morpfw.Schema):

    name: typing.Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "editable": False,
            "searchable": True,
            "validators": [valid_namespaced_identifier],
        },
    )

    title: typing.Optional[str] = field(
        default=None, metadata={"required": True, "searchable": True}
    )
    description: typing.Optional[str] = field(default=None, metadata={"format": "text"})
    type: typing.Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "editable": False,
            "searchable": True,
            "validators": [valid_type],
            "deform.widget": Select2Widget(
                values=[("", "")] + list(ACCEPTED_TYPES), placeholder=" "
            ),
        },
    )
    notes: typing.Optional[str] = field(
        default=None,
        metadata={
            "format": "text/html",
            "preparers": [HTMLSanitizer()],
            "deform.widget": RichTextWidget(),
        },
    )
    code: typing.Optional[str] = field(
        default="def validate(value):\n    return True",
        metadata={
            "format": "text/python",
            "required": True,
            "deform.widget": CodeWidget(),
        },
    )
    error_message: typing.Optional[str] = field(
        default=None, metadata={"required": True}
    )
