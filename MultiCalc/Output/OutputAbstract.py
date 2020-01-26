from abc import abstractmethod


class OutputAbstract:

    @abstractmethod
    def append(self, value):
        pass
