from abc import ABCMeta, abstractmethod
import pickle
import json


class SerializationInterface(metaclass=ABCMeta):
    @abstractmethod
    def serialize(self, data):
        ...

    @abstractmethod
    def deserialize(self, file_name):
        ...


class SerializeJson(SerializationInterface):
    def serialize(self, data):
        with open('data.json', 'w') as f:
            json.dump(data, f)

    def deserialize(self, file_name):
        with open(file_name, 'r') as f:
            deserialize_json = json.load(f)
        return deserialize_json


class SerializeBin(SerializationInterface):
    def serialize(self, data):
        with open('data.bin', 'wb') as f:
            pickle.dump(data, f)

    def deserialize(self, file_name):
        with open(file_name, 'rb') as f:
            deserialize_pickle = pickle.load(f)
        return deserialize_pickle


if __name__=="__main__":

    data = {'Atos': (1, 2, 3), 'Portos': [1, 2, 3], 'Aramis': 'abracadabra'}

    a = SerializeJson()
    a.serialize(data)
    a.deserialize("data.json")

    b = SerializeBin()
    b.serialize(data)
    b.deserialize("data.bin")
