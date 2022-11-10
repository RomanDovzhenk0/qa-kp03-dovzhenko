import pytest

from exceptions import FileAlreadyExistError
from exceptions import InvalidPathError
from main import FileSystem


def test_create_buffer_file_throw_exception_if_path_invalid():
    with pytest.raises(InvalidPathError):
        file_system = FileSystem()
        file_system.mkdir("/a")
        file_system.createBufferFile("/a/b/log.txt")  # InvalidPathError


def test_create_buffer_file_throw_exception_if_file_already_exist():
    with pytest.raises(FileAlreadyExistError):
        file_system = FileSystem()
        file_system.mkdir("/a")
        file_system.createBufferFile("/a/log.txt")
        file_system.createBufferFile("/a/log.txt")  # FileAlreadyExistError


def test_create_buffer_file_success():
    file_system = FileSystem()
    file_system.mkdir("/a")
    file_system.createBufferFile("/a/logA1.txt")
    file_system.createBufferFile("/a/logA2.txt")
    file_system.mkdir("/b")
    file_system.createBufferFile("/b/logB1.txt")
    file_system.createBufferFile("/b/logB2.txt")
    assert file_system.ls("/a") == ['logA1.txt', 'logA2.txt']
    assert file_system.ls("/b") == ['logB1.txt', 'logB2.txt']
