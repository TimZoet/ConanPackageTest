from conans import ConanFile
from conans.tools import load
from conan.tools.cmake import CMakeToolchain, CMake
from conan.tools.layout import cmake_layout

class Package2Conan(ConanFile):
    name = "package2"
    version = "1.0.0"
    requires = "package1/1.0.0@timzoet/stable"
    generators = "cmake_find_package"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    exports_sources = "CMakeLists.txt", "include/*", "src/*", "PackageConfigTemplate.cmake.in"

    def layout(self):
        cmake_layout(self)
    
    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["package2"]
