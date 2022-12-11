import pytest

from exceptions import FileAlreadyExistError
from exceptions import InvalidPathError
from main import FileSystem


def test_create_file_throw_exception_if_path_invalid():
    with pytest.raises(InvalidPathError):
        file_system = FileSystem()
        file_system.mkdir("/a")
        file_system.create_file("/a/b/log.txt")  # InvalidPathError


def test_create_file_throw_exception_if_file_already_exist():
    with pytest.raises(FileAlreadyExistError):
        file_system = FileSystem()
        file_system.mkdir("/a")
        file_system.create_file("/a/log.txt")
        file_system.create_file("/a/log.txt")  # FileAlreadyExistError


def test_create_file_success():
    file_system = FileSystem()
    file_system.mkdir("/a")
    file_system.create_file("/a/logA1.txt")
    file_system.create_file("/a/logA2.txt")
    file_system.mkdir("/b")
    file_system.create_file("/b/logB1.txt")
    file_system.create_file("/b/logB2.txt")
    assert file_system.ls("/a") == ['logA1.txt', 'logA2.txt']
    assert file_system.ls("/b") == ['logB1.txt', 'logB2.txt']
