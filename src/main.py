from src.dialog.formdoc.FormDocContainer import FormDocContainer
from src.dialog.managecase.ManageCaseContainer import ManageCaseContainer
from src.dialog.pickuser.PickUserContainer import PickUserContainer
from src.dialog.table.TableContainer import TableContainer
from src.dialog.tkinter.DialogFactoryTkinter import DialogFactoryTkinter
from src.session.Session import Session
from src.storage.case.CaseStorageJson import CaseStorageJson
from src.storage.config.ConfigStorageJson import ConfigStorageJson

json_resources_folder = "../resources/"

session = Session()
config_storage = ConfigStorageJson(json_resources_folder + "config.json")
case_storage = CaseStorageJson(json_resources_folder + "cases.json")
dialog_factory = DialogFactoryTkinter()

manage_case_container = ManageCaseContainer(session, case_storage, dialog_factory)
form_doc_container = FormDocContainer(dialog_factory)
table_container = TableContainer(manage_case_container, form_doc_container, session, case_storage, dialog_factory)
pick_user_container = PickUserContainer(table_container, config_storage, session, dialog_factory)

pick_user_container.show_dialog()
