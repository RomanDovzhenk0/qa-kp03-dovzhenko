import pytest

from exceptions import InvalidPathError
from main import FileSystem


def test_move_node_success():
    file_system = FileSystem()
    file_system.mkdir("/a/b")
    file_system.mkdir("/a/c")
    file_system.moveNode("/a/b", "/a/c")
    assert file_system.ls("/a/c") == ['b']
    assert file_system.ls("/a") == ['c']
    with pytest.raises(InvalidPathError):
        file_system.ls("/a/b")


def test_move_node_throw_exception_if_new_path_start_with_old_path():
    file_system = FileSystem()
    file_system.mkdir("/a/b")
    file_system.mkdir("/a/b/c")
    with pytest.raises(InvalidPathError):
        file_system.moveNode("/a/b", "/a/b/c")


def test_delete_node_throw_exception_if_new_path_invalid():
    file_system = FileSystem()
    file_system.mkdir("/a/b")
    with pytest.raises(InvalidPathError):
        file_system.moveNode("/a/b", "/a/c")


def test_delete_node_throw_exception_if_old_path_invalid():
    file_system = FileSystem()
    file_system.mkdir("/a/c")
    with pytest.raises(InvalidPathError):
        file_system.moveNode("/a/b", "/a/c")
