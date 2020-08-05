class Session:

    def __init__(self):
        self.__employee_id = ""

    def set_employee_id(self, employee_id: str):
        self.__employee_id = employee_id

    def get_employee_id(self):
        return self.__employee_id
