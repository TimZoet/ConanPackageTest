cmake_minimum_required(VERSION 3.15)

project(TestProject VERSION 1.0.0 LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)

find_package(package2 REQUIRED)

add_executable(app main.cpp)
target_link_libraries(app PUBLIC package2::package2)
