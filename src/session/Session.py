class Session:

    def __init__(self):
        self.__employee_id = ""
        self.__case_id = ""

    def set_employee_id(self, employee_id: str):
        self.__employee_id = employee_id

    def get_employee_id(self):
        return self.__employee_id

    def set_case_id(self, case_id: str):
        self.__case_id = case_id

    def get_case_id(self):
        return self.__case_id
