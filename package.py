# -*- coding: utf-8 -*-

name = "opensubdiv"

version = "3.3.3"

authors = ["Pixar Animation Studio"]

requires = [
    "tbb-4.4.6",
    "glew-2.0.0",
    "glfw-3.3.0",
    "ptex-2.3.2",
]

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")

uuid = "repository.opensubdiv"
