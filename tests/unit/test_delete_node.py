import pytest

from exceptions import InvalidPathError
from main import FileSystem


def test_delete_node_success():
    file_system = FileSystem()
    file_system.mkdir("/a/b")
    file_system.mkdir("/a/c")
    file_system.mkdir("/a/c/d")
    file_system.mkdir("/a/d")
    file_system.delete_node("/a/c")
    assert file_system.ls("/a") == ['b', 'd']
    with pytest.raises(InvalidPathError):
        file_system.ls("/a/c")


def test_delete_node_throw_exception_if_path_invalid():
    file_system = FileSystem()
    file_system.mkdir("/a/b")
    file_system.mkdir("/a/c")
    file_system.mkdir("/a/c/d")
    with pytest.raises(InvalidPathError):
        file_system.delete_node("/a/d")

