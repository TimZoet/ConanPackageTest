cmake_minimum_required(VERSION 3.15)

project(TestProject VERSION 1.0.0 LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)

set(NAME "package1")
set(EXPORT_NAME "${NAME}Targets")
set(INCLUDE_DIR "include/package1")
set(SRC_DIR "src")
set(HEADERS ${INCLUDE_DIR}/lib.h)
set(SOURCES ${SRC_DIR}/lib.cpp)

add_library(${NAME} STATIC ${HEADERS} ${SOURCES})

target_include_directories(${NAME} PUBLIC
    "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>"
    "$<INSTALL_INTERFACE:include>"
)

install(
    TARGETS ${NAME}
    EXPORT ${EXPORT_NAME}
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
    INCLUDES DESTINATION include
)

install(
    FILES ${HEADERS}
    DESTINATION include/${NAME}
)

install(
    EXPORT ${EXPORT_NAME}
    FILE "${EXPORT_NAME}.cmake"
    NAMESPACE "${NAME}::"
    DESTINATION lib/cmake/${NAME}
)

include(CMakePackageConfigHelpers)

configure_package_config_file(
    ${CMAKE_SOURCE_DIR}/PackageConfigTemplate.cmake.in
    "${CMAKE_CURRENT_BINARY_DIR}/${NAME}Config.cmake"
    INSTALL_DESTINATION lib/cmake/${NAME}
)

write_basic_package_version_file(
    "${CMAKE_CURRENT_BINARY_DIR}/${NAME}ConfigVersion.cmake"
    VERSION ${VERSION}
    COMPATIBILITY AnyNewerVersion
)

install(
    FILES
        "${CMAKE_CURRENT_BINARY_DIR}/${NAME}Config.cmake"
        "${CMAKE_CURRENT_BINARY_DIR}/${NAME}ConfigVersion.cmake"
    DESTINATION lib/cmake/${NAME}
)
