from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class JuceRecipe(ConanFile):
    name = "juce_recipe"
    version = "0.0.1"
    package_type = "application"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    requires = "juce/7.0.5@juce/release" # Require JUCE
    default_options = {                  # Configure it
        "juce/*:build_extras": True
    }

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*"

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generator = "Xcode"
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
