
class User:

    def __init__(self, name, last_name):
        self.__id = self.__generate_id()
        self.name = name
        self.last_name = last_name


    def __generate_id(self):
        from uvid import uvid4

        return str(uvid4())


    @property
    def id(self):
        return self.__id




































