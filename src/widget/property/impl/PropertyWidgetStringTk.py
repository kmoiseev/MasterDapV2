from tkinter import Tk, Label, Entry, END

from src.property.PropertyValue import PropertyValue
from src.template.property.PropertyTemplate import PropertyTemplate
from src.widget.property.impl.PropertyWidgetTk import PropertyWidgetTk


class PropertyWidgetStringTk(PropertyWidgetTk):

    def __init__(self, prop_tmpl: PropertyTemplate):
        super().__init__(prop_tmpl)
        self.txt = None

    def make(self, tk: Tk, grid_row_number):
        lbl = Label(tk, text=self.prop_tmpl.id)
        lbl.grid(column=0, row=grid_row_number)

        self.txt = Entry(tk, width=10)
        self.txt.grid(column=1, row=grid_row_number)

    def set_val(self, val: PropertyValue):
        self.txt.delete(0, END)
        self.txt.insert(0, val.value)

    def get_val(self) -> PropertyValue:
        return PropertyValue(self.txt.get())
