from abc import ABC, abstractmethod


class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass


class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None


class Stack(StackInterface):
    def __init__(self):
        self._top = None
        self._last = None

    def push_back(self, obj):
        if not self._top:
            self._top, self._last = obj, obj
        else:
            self._last._next = obj
            self._last = obj

    def pop_back(self):
        p_obj = self._last
        if self._top is self._last:
            self._top, self._last = None, None
        else:
            obj = self._top
            while obj._next != self._last:
                obj = obj._next
            self._last = obj
            self._last._next = None

        return p_obj




