import pytest

from exceptions import InvalidPathError
from main import FileSystem


def test_mkdir_success():
    file_system = FileSystem()
    file_system.mkdir("/a")
    file_system.mkdir("/a/b")
    file_system.mkdir("/a/c")
    file_system.mkdir("/b/a")
    file_system.mkdir("/b/c")
    assert file_system.ls("/") == ['a', 'b']
    assert file_system.ls("/a") == ['b', 'c']
    assert file_system.ls("/b") == ['a', 'c']


def test_mkdir_throws_exception_if_path_contain_file():
    with pytest.raises(InvalidPathError):
        file_system = FileSystem()
        file_system.mkdir("/a")
        file_system.createFile("/a/file.txt")
        file_system.mkdir("/a/file.txt/b")  # InvalidPathError


def test_mkdir_throws_exception_if_path_not_start_with_slash():
    with pytest.raises(InvalidPathError):
        file_system = FileSystem()
        file_system.mkdir("a/b")  # InvalidPathError


def test_mkdir_throws_exception_if_path_contain_empty_dir_name():
    with pytest.raises(InvalidPathError):
        file_system = FileSystem()
        file_system.mkdir("/a//b")  # InvalidPathError
