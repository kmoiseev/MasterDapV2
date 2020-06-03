from abc import abstractmethod

from src.dialog.formdoc.FormDocDialog import FormDocDialog
from src.dialog.formdoc.FormDocFuncs import FormDocFuncs
from src.dialog.managecase.ManageCaseDialog import ManageCaseDialog
from src.dialog.managecase.ManageCaseFuncs import ManageCaseFuncs
from src.dialog.pickuser.PickUserDialog import PickUserDialog
from src.dialog.pickuser.PickUserFuncs import PickUserFuncs
from src.dialog.table.TableDialog import TableDialog
from src.dialog.table.TableFuncs import TableFuncs


class DialogFactory:

    @abstractmethod
    def create_table_dialog(self, table_funcs: TableFuncs) -> TableDialog:
        pass

    @abstractmethod
    def create_pick_user_dialog(self, pick_user_funcs: PickUserFuncs) -> PickUserDialog:
        pass

    @abstractmethod
    def create_manage_case_dialog(self, manage_case_funcs: ManageCaseFuncs) -> ManageCaseDialog:
        pass

    @abstractmethod
    def create_form_doc_dialog(self, form_doc_funcs: FormDocFuncs) -> FormDocDialog:
        pass
