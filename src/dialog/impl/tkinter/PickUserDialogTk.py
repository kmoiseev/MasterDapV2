from abc import ABC
from tkinter import Tk, Frame, W, N, E, S, StringVar, OptionMenu, Label, Button
from typing import List

from src.dialog.common.pick_user.PickUserDialog import PickUserDialog
from src.dialog.common.pick_user.PickUserFuncs import PickUserFuncs
from src.storage.common.user.User import User


class PickUserDialogTk(PickUserDialog, ABC):

    def __init__(self, pick_user_funcs: PickUserFuncs):
        super().__init__(pick_user_funcs)
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.funcs.closed_on_x)
        # Подготавливаем данные о пользователях для выпадающего списка
        users: List[User] = self.funcs.get_users()
        self.user_keys_by_names = {users[i].props["user_name"].get_val(): users[i].key for i in range(0, len(users))}
        self.first_user_name = users[0].props["user_name"].get_val()

    def show(self):
        self.root.title("Pick User")
        mainframe = Frame(self.root)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe.pack(pady=100, padx=100)

        tkvar = StringVar(self.root)
        choices = self.user_keys_by_names
        tkvar.set(self.first_user_name)
        popupMenu = OptionMenu(mainframe, tkvar, *choices)

        Label(mainframe, text="Choose a dish").grid(row=1, column=1)
        popupMenu.grid(row=2, column=1)

        button = Button(self.root, text='My Button', width=40, height=3, bg='#0052cc', fg='#ffffff',
                        activebackground='#0052cc', activeforeground='#aaffaa',
                        command=lambda: self.funcs.user_selected(self.user_keys_by_names[tkvar.get()]))
        button.pack()
        self.root.mainloop()

    def close(self):
        self.root.destroy()
