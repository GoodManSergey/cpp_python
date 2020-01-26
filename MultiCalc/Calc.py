from MultiProc import MultiProc
from Input.InputFileSimple import InputFileSimple
from Output.OutputFileSimple import OutputFileSimple
from Calc import get_simple
import sys


if __name__ == '__main__':
    input = InputFileSimple(sys.argv[1])
    output = OutputFileSimple(sys.argv[2])
    multi = MultiProc(get_simple, input, output)
    multi.process()
