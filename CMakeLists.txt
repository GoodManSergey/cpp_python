cmake_minimum_required(VERSION 3.0)
set(python_version "3.5.2" CACHE STRING "Specify which Python version to use")
find_package(PythonLibs 35 REQUIRED)
find_package(Boost COMPONENTS python-py35 REQUIRED)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
if(UNIX)
    set(BOOST_PYTHONLIB boost_python-py35)
else()
    set(BOOST_PYTHONLIB boost_python-py35)
endif()

python_add_module(Calc src/Calc.cpp)

target_include_directories(Calc PUBLIC
        ${Boost_INCLUDE_DIRS} ${PYTHON_INCLUDE_DIRS})
target_link_libraries(Calc
        ${Boost_LIBRARIES} ${PYTHON_LIBRARIES})
target_link_libraries(Calc ${BOOST_PYTHONLIB})