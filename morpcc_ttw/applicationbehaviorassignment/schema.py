import typing
from dataclasses import dataclass, field

import morpfw
from morpcc.deform.referencewidget import ReferenceWidget
from morpcc.deform.vocabularywidget import VocabularyWidget
from morpcc.validator.reference import ReferenceValidator
from morpcc.validator.vocabulary import VocabularyValidator


@dataclass
class ApplicationBehaviorAssignmentSchema(morpfw.Schema):

    behavior: typing.Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "validators": [VocabularyValidator("morpcc.application_behaviors")],
            "deform.widget": VocabularyWidget("morpcc.application_behaviors"),
        },
    )
    application_uuid: typing.Optional[str] = field(
        default=None,
        metadata={
            "title": "Application",
            "format": "uuid",
            "required": True,
            "validators": [ReferenceValidator("morpcc.application", "uuid")],
            "deform.widget": ReferenceWidget("morpcc.application", "title", "uuid"),
        },
    )
