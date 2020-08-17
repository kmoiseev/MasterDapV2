from src.dialog.common.formdoc.FormDocContainer import FormDocContainer
from src.dialog.common.manageentity.ManageEntityContainer import ManageEntityContainer
from src.dialog.common.pickuser.PickUserContainer import PickUserContainer
from src.dialog.common.table.TableContainer import TableContainer
from src.dialog.impl.tkinter.DialogFactoryTkinter import DialogFactoryTkinter
from src.session.inmemory.SessionInMemory import SessionInMemory
from src.storage.impl.json.ConfigStorageJson import ConfigStorageJson
from src.storage.impl.json.EntityStorageJson import EntityStorageJson

json_resources_folder = "../resources/"

session = SessionInMemory()
config_storage = ConfigStorageJson(json_resources_folder + "config.json")
case_storage = EntityStorageJson(json_resources_folder + "cases.json")
dialog_factory = DialogFactoryTkinter()

manage_case_container = ManageEntityContainer(session, case_storage, dialog_factory)
form_doc_container = FormDocContainer(dialog_factory)
table_container = TableContainer(manage_case_container, form_doc_container, session, case_storage, dialog_factory)
pick_user_container = PickUserContainer(table_container, config_storage, session, dialog_factory)

pick_user_container.show_dialog()
