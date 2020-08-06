from src.dialog.common.DialogFactory import DialogFactory
from src.dialog.common.formdoc import FormDocDialog
from src.dialog.common.formdoc import FormDocFuncs
from src.dialog.common.manageentity import ManageCaseDialog
from src.dialog.common.manageentity import ManageEntityFuncs
from src.dialog.common.pickuser.PickUserDialog import PickUserDialog
from src.dialog.common.pickuser.PickUserFuncs import PickUserFuncs
from src.dialog.common.table.TableDialog import TableDialog
from src.dialog.common.table.TableFuncs import TableFuncs
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
