from Output.OutputAbstract import OutputAbstract


class OutputFileSimple(OutputAbstract):
    def __init__(self, filename):
        self.__file = open(filename, 'w')

    def __del__(self):
        self.__file.close()

    def append(self, value):
        string = str(value.get("input")) + "=" + "*".join(str(x) for x in value.get("res"))
        self.__file.write(string)
        self.__file.write("\n")
