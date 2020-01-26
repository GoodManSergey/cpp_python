from Input.InputAbstract import InputAbstract


class InputFileSimple(InputAbstract):
    def __init__(self, filename):
        self.__file = open(filename, 'r')

    def __del__(self):
        self.__file.close()

    def __iter__(self):
        return self

    def __next__(self):
        string = self.__file.readline().strip()
        if string:
            return int(string)
        else:
            raise StopIteration
