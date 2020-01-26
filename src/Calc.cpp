#include <boost/python.hpp>
#include <Python.h>


boost::python::list get_simple(unsigned long long int value) {
    boost::python::list result_list;
    unsigned long long int number = 2;
    while (value >= number) {
        if (value % number == 0) {
            result_list.append(number);
            value /= number;
            continue;
        } else {
            number++;
            continue;
        }
    }
    return result_list;
}

using namespace boost::python;

BOOST_PYTHON_MODULE(Calc)
{
    def("get_simple", get_simple);
};
