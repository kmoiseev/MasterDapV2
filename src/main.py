from src.dialog.common.formdoc import FormDocContainer
from src.dialog.common.manageentity import ManageEntityContainer
from src.dialog.common.pickuser.PickUserContainer import PickUserContainer
from src.dialog.common.table.TableContainer import TableContainer
from src.dialog.impl.tkinter import DialogFactoryTkinter
from src.session.Session import Session
from src.storage.entity.EntityStorageJson import EntityStorageJson
from src.storage.config.ConfigStorageJson import ConfigStorageJson

json_resources_folder = "../resources/"

session = Session()
config_storage = ConfigStorageJson(json_resources_folder + "config.json")
case_storage = EntityStorageJson(json_resources_folder + "cases.json")
dialog_factory = DialogFactoryTkinter()

manage_case_container = ManageEntityContainer(session, case_storage, dialog_factory)
form_doc_container = FormDocContainer(dialog_factory)
table_container = TableContainer(manage_case_container, form_doc_container, session, case_storage, dialog_factory)
pick_user_container = PickUserContainer(table_container, config_storage, session, dialog_factory)

pick_user_container.show_dialog()
