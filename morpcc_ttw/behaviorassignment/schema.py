import typing
from dataclasses import dataclass, field

import morpfw
from morpcc.deform.referencewidget import ReferenceWidget
from morpcc.deform.vocabularywidget import VocabularyWidget
from morpcc.validator.reference import ReferenceValidator
from morpcc.validator.vocabulary import VocabularyValidator


@dataclass
class BehaviorAssignmentSchema(morpfw.Schema):

    behavior: typing.Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "validators": [VocabularyValidator("morpcc.behaviors")],
            "deform.widget": VocabularyWidget("morpcc.behaviors"),
        },
    )
    entity_uuid: typing.Optional[str] = field(
        default=None,
        metadata={
            "title": "Entity",
            "format": "uuid",
            "required": True,
            "validators": [ReferenceValidator("morpcc.entity", "uuid")],
            "deform.widget": ReferenceWidget("morpcc.entity", "title", "uuid"),
        },
    )
