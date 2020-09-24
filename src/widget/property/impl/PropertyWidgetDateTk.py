from tkinter import Widget, Entry, Label, Tk

from src.property.PropertyValue import PropertyValue
from src.widget.property.impl.PropertyWidgetTk import PropertyWidgetTk


class PropertyWidgetDateTk(PropertyWidgetTk):

    def make(self, tk: Tk, grid_row_number):
        lbl = Label(tk, text=self.prop_tmpl.id)
        lbl.grid(column=0, row=grid_row_number)

        txt = Entry(tk, width=10)
        txt.grid(column=1, row=grid_row_number)

    def set_val(self, val: PropertyValue):
        pass

    def get_val(self) -> PropertyValue:
        pass
