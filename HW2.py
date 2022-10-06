from abc import ABCMeta, abstractmethod
import pickle


class OutputABC(metaclass=ABCMeta):
    def __init__(self, data, name):
        self.data = data
        self.__name = None
        self.name = name

    @abstractmethod
    def output(self):
        pass


class OutputAddressBook(OutputABC):
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        parse = name.split('.')
        if parse[1] == 'bin':
            self.__name = name
        else:
            raise SyntaxError("Must be 'bin' file format")

    def output(self):
        with open(self.__name, 'rb') as f:
            unpack = pickle.load(f)
            print(unpack)


class OutputNote(OutputABC):
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        parse = name.split('.')
        if parse[1] == 'bin':
            self.__name = name
        else:
            raise SyntaxError("Must be 'bin' file format")

    def output(self):
        with open(self.__name, 'rb') as f:
            unpack = pickle.load(f)
            print(unpack)
