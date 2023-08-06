cmake_minimum_required(VERSION 3.20.0)
project(TestPackage CXX)

add_executable(test_package test_package.cpp)

find_package(dspbb CONFIG REQUIRED)
target_link_libraries(test_package dspbb::dspbb)
target_compile_features(test_package PUBLIC cxx_std_17)
