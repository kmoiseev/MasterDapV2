from enum import Enum

from src.template.property.impl.PropertyTemplateDate import PropertyTemplateDate
from src.template.property.impl.PropertyTemplateDropdown import PropertyTemplateDropdown
from src.template.property.impl.PropertyTemplateString import PropertyTemplateString


class PropertyType(Enum):
    DATE = PropertyTemplateDate
    DROPDOWN = PropertyTemplateDropdown
    STRING = PropertyTemplateString
