# -*- coding: utf-8 -*-

name = "opensubdiv"

version = "3.3.3"

authors = ["Pixar Animation Studio"]

requires = [
    "ptex",
    "tbb",
    "glew",
    "glfw",
]

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")

uuid = "repository.opensubdiv"
