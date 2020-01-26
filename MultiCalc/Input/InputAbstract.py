from abc import abstractmethod


class InputAbstract:

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __next__(self):
        pass
