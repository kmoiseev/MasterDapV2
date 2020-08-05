from src.dialog.DialogFactory import DialogFactory
from src.dialog.formdoc.FormDocDialog import FormDocDialog
from src.dialog.formdoc.FormDocFuncs import FormDocFuncs
from src.dialog.manageentity.ManageCaseDialog import ManageCaseDialog
from src.dialog.manageentity.ManageEntityFuncs import ManageEntityFuncs
from src.dialog.pickuser.PickUserDialog import PickUserDialog
from src.dialog.pickuser.PickUserFuncs import PickUserFuncs
from src.dialog.table.TableDialog import TableDialog
from src.dialog.table.TableFuncs import TableFuncs
from src.dialog.impl.tkinter.FormDocDialogTk import FormDocDialogTk
from src.dialog.impl.tkinter import ManageCaseDialogTk
from src.dialog.impl.tkinter import PickUserDialogTk
from src.dialog.impl.tkinter import TableDialogTk


class DialogFactoryTkinter(DialogFactory):
    def create_table_dialog(self, table_funcs: TableFuncs) -> TableDialog:
        return TableDialogTk(table_funcs)

    def create_pick_user_dialog(self, pick_user_funcs: PickUserFuncs) -> PickUserDialog:
        return PickUserDialogTk(pick_user_funcs)

    def create_manage_case_dialog(self, manage_case_funcs: ManageEntityFuncs) -> ManageCaseDialog:
        return ManageCaseDialogTk(manage_case_funcs)

    def create_form_doc_dialog(self, form_doc_funcs: FormDocFuncs) -> FormDocDialog:
        return FormDocDialogTk(form_doc_funcs)
