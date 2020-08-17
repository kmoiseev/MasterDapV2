from abc import abstractmethod

from src.dialog.common.formdoc import FormDocDialog
from src.dialog.common.formdoc import FormDocFuncs
from src.dialog.common.manageentity import ManageEntityDialog
from src.dialog.common.manageentity import ManageEntityFuncs
from src.dialog.common.pickuser.PickUserDialog import PickUserDialog
from src.dialog.common.pickuser.PickUserFuncs import PickUserFuncs
from src.dialog.common.table.TableDialog import TableDialog
from src.dialog.common.table.TableFuncs import TableFuncs


class DialogFactory:

    @abstractmethod
    def create_table_dialog(self, table_funcs: TableFuncs) -> TableDialog:
        pass

    @abstractmethod
    def create_pick_user_dialog(self, pick_user_funcs: PickUserFuncs) -> PickUserDialog:
        pass

    @abstractmethod
    def create_manage_case_dialog(self, manage_case_funcs: ManageEntityFuncs) -> ManageEntityDialog:
        pass

    @abstractmethod
    def create_form_doc_dialog(self, form_doc_funcs: FormDocFuncs) -> FormDocDialog:
        pass
