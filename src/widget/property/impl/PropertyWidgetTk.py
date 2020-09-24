from abc import ABC, abstractmethod
from tkinter import Tk, Widget

from src.widget.property.common.PropertyWidget import PropertyWidget


class PropertyWidgetTk(PropertyWidget, ABC):

    @abstractmethod
    def make(self, tk: Tk, grid_row_number):
        pass
