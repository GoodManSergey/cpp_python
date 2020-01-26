#include <boost/python.hpp>
#include <math.h>
#include <Python.h>


boost::python::list get_simple(unsigned long long int value) {
    boost::python::list result_list;
    unsigned long long int number = 2;
    unsigned long long int border = sqrt(value);
    while (border > number) {
        if (value % number == 0) {
            result_list.append(number);
            value /= number;
            border = sqrt(value);
            continue;
        } else {
            number++;
            continue;
        }
    }
    if (value != 1)
        result_list.append(value);
    return result_list;
}

using namespace boost::python;

BOOST_PYTHON_MODULE(Calc)
{
    def("get_simple", get_simple);
};
