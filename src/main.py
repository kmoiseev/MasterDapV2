from src.dialog.common.formdoc.FormDocContainer import FormDocContainer
from src.dialog.common.manageentity.ManageEntityContainer import ManageEntityContainer
from src.dialog.common.pickuser.PickUserContainer import PickUserContainer
from src.dialog.common.table.TableContainer import TableContainer
from src.dialog.common.table.data.TableFactory import TableFactory
from src.dialog.impl.tkinter.DialogFactoryImpl import DialogFactoryImpl
from src.session.common.Session import Session
from src.session.impl.inmemory.SessionInMemory import SessionInMemory
from src.storage.common.entity.EntityFactory import EntityFactory
from src.storage.common.user.UserFactory import UserFactory
from src.storage.impl.json.EntityStorageJson import EntityStorageJson
from src.storage.impl.json.UserStorageJson import UserStorageJson
from src.template.TemplateManager import TemplateManager
from src.template.property.PropertyTypeConfig import PropertyTypeConfig

resources_folder = '../resources/'

property_type_config_folder = resources_folder + 'propertytypeconfig/'
template_folder = resources_folder + 'template/'
storage_folder = resources_folder + 'jsonstorage/'

# PropertyTypeConfig - для настройки типов свойств. Например, там настраиваются
# значения для выпадающих списков
property_type_config = PropertyTypeConfig(property_type_config_folder)
# TemplateManager - для загрузки и хранения всех шаблонов свойств
template_manager = TemplateManager(template_folder, property_type_config)

# SessionInMemory - сессия, которая хранится только внутри оперативной памяти
session: Session = SessionInMemory()

# UserFactory - создаёт объекты пользователей
user_factory = UserFactory(template_manager.user_template)
# UserStorageJson - хранилище пользователей и информации о них
user_storage = UserStorageJson(storage_folder + "users.json", user_factory)

entity_factory = EntityFactory(template_manager.entity_template)
# EntityStorageJson - хранилище сущностей (дел) и информации о них
entity_storage = EntityStorageJson(storage_folder + "entities.json", entity_factory)

# TableFactory - фабрика табличных данных
table_factory = TableFactory(template_manager.table_template)

# DialogFactoryTkinter - фабрика диалогов на Tkinter библиотеке
dialog_factory = DialogFactoryImpl()

manage_case_container = ManageEntityContainer(
    session,
    entity_storage,
    dialog_factory,
    entity_factory,
    template_manager.entity_template
)
form_doc_container = FormDocContainer(
    dialog_factory, session
)
table_container = TableContainer(
    manage_case_container,
    form_doc_container,
    session,
    entity_storage,
    dialog_factory,
    table_factory
)
pick_user_container = PickUserContainer(
    table_container,
    user_storage,
    session,
    dialog_factory
)

pick_user_container.show_dialog()
