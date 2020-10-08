from src.dialog.common.DialogFactory import DialogFactory
from src.dialog.common.form_doc.FormDocDialog import FormDocDialog
from src.dialog.common.form_doc.FormDocFuncs import FormDocFuncs
from src.dialog.common.manage_entity.ManageEntityDialog import ManageEntityDialog
from src.dialog.common.manage_entity.ManageEntityFuncs import ManageEntityFuncs
from src.dialog.common.pick_user.PickUserDialog import PickUserDialog
from src.dialog.common.pick_user.PickUserFuncs import PickUserFuncs
from src.dialog.common.table.TableDialog import TableDialog
from src.dialog.common.table.TableFuncs import TableFuncs
from src.dialog.impl.tkinter.FormDocDialogTk import FormDocDialogTk
from src.dialog.impl.tkinter.ManageEntityDialogTk import ManageEntityDialogTk
from src.dialog.impl.tkinter.PickUserDialogTk import PickUserDialogTk
from src.dialog.impl.pyqt.TableDialogPyQt import TableDialogPyQt


class DialogFactoryImpl(DialogFactory):

    def __init__(self):
        pass

    def create_table_dialog(self, table_funcs: TableFuncs) -> TableDialog:
        return TableDialogPyQt(table_funcs)

    def create_pick_user_dialog(self, pick_user_funcs: PickUserFuncs) -> PickUserDialog:
        return PickUserDialogTk(pick_user_funcs)

    def create_manage_case_dialog(self, manage_entity_funcs: ManageEntityFuncs) -> ManageEntityDialog:
        return ManageEntityDialogTk(manage_entity_funcs)

    def create_form_doc_dialog(self, form_doc_funcs: FormDocFuncs) -> FormDocDialog:
        return FormDocDialogTk(form_doc_funcs)
