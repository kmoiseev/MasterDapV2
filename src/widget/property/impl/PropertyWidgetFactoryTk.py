from typing import Dict

from src.template.property.PropertyTemplate import PropertyTemplate
from src.template.property.impl.PropertyTemplateDate import PropertyTemplateDate
from src.template.property.impl.PropertyTemplateDropdown import PropertyTemplateDropdown
from src.template.property.impl.PropertyTemplateString import PropertyTemplateString
from src.widget.property.impl.PropertyWidgetDateTk import PropertyWidgetDateTk
from src.widget.property.impl.PropertyWidgetDropdownTk import PropertyWidgetDropdownTk
from src.widget.property.impl.PropertyWidgetStringTk import PropertyWidgetStringTk
from src.widget.property.impl.PropertyWidgetTk import PropertyWidgetTk


class PropertyWidgetFactoryTk:
    widget_mappings: Dict[type(PropertyTemplate), type(PropertyWidgetTk)] = \
        {
            PropertyTemplateString: PropertyWidgetStringTk,
            PropertyTemplateDate: PropertyWidgetDateTk,
            PropertyTemplateDropdown: PropertyWidgetDropdownTk
        }

    @staticmethod
    def create(prop_tmpl: PropertyTemplate) -> PropertyWidgetTk:
        return PropertyWidgetFactoryTk.widget_mappings[type(prop_tmpl)](prop_tmpl)
