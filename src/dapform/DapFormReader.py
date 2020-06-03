from src.dapform.DapFormDrawer import DapFormDrawer


class DapFormReader:

    def __init__(self, path_to_form: str, drawer: DapFormDrawer):
        self.__path_to_form = path_to_form
        self.__drawer = drawer

    def draw(self):
        pass

    def read_size(self, ) -> (int, int):
        pass

    def read_template(self):
        pass