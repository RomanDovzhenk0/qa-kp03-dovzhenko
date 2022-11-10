import pytest

from exceptions import FileAlreadyExistError
from exceptions import InvalidPathError
from main import FileSystem


def test_create_buffer_file_throw_exception_if_path_invalid():
    with pytest.raises(InvalidPathError):
        file_system = FileSystem()
        file_system.mkdir("/a")
        file_system.createBinaryFile("/a/b/log.txt", "Content#1")  # InvalidPathError


def test_create_buffer_file_throw_exception_if_file_already_exist():
    with pytest.raises(FileAlreadyExistError):
        file_system = FileSystem()
        file_system.mkdir("/a")
        file_system.createBinaryFile("/a/log.txt", "Content#1")
        file_system.createBinaryFile("/a/log.txt", "Content#2")  # FileAlreadyExistError


def test_create_buffer_file_success():
    file_system = FileSystem()
    file_system.mkdir("/a")
    file_system.createBinaryFile("/a/logA1.txt", "Content#A1")
    file_system.createBinaryFile("/a/logA2.txt", "Content#A2")
    file_system.mkdir("/b")
    file_system.createBinaryFile("/b/logB1.txt", "Content#B1")
    file_system.createBinaryFile("/b/logB2.txt", "Content#B2")
    assert file_system.ls("/a") == ['logA1.txt', 'logA2.txt']
    assert file_system.ls("/b") == ['logB1.txt', 'logB2.txt']
