cmake_minimum_required(VERSION 3.15...3.22)
project(example LANGUAGES CXX)

find_package(Python 3.6 COMPONENTS Interpreter Development REQUIRED)
find_package(pybind11 CONFIG REQUIRED)
# or add_subdirectory(pybind11)

pybind11_add_module(example example.cpp)