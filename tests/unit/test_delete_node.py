import pytest

from FileSystemService import FileSystemService
from FileAlreadyExistError import FileAlreadyExistError
from FileSystemService import FileSystemService
from InvalidPathError import InvalidPathError


def test_delete_node_success():
    file_system = FileSystemService()
    file_system.mkdir("/a/b")
    file_system.mkdir("/a/c")
    file_system.mkdir("/a/c/d")
    file_system.mkdir("/a/d")
    file_system.delete_node("/a/c")
    assert file_system.ls("/a") == ['b', 'd']
    with pytest.raises(InvalidPathError):
        file_system.ls("/a/c")


def test_delete_node_throw_exception_if_path_invalid():
    file_system = FileSystemService()
    file_system.mkdir("/a/b")
    file_system.mkdir("/a/c")
    file_system.mkdir("/a/c/d")
    with pytest.raises(InvalidPathError):
        file_system.delete_node("/a/d")

