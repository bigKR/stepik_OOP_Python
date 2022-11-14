from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return "Базовый класс Model"


class ModelForm(Model):
    _id = 0

    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = self.set_pk()

    @classmethod
    def set_pk(cls):
        cls._id += 1
        return cls._id

    def get_pk(self):
        return self._id


