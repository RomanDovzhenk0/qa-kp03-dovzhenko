import pytest

from exceptions import InvalidPathError
from main import FileSystem


def test_add_content_to_file_throw_exception_if_file_path_invalid():
    file_system = FileSystem()
    file_system.mkdir("/a")
    file_system.createFile("/a/log.txt")
    with pytest.raises(InvalidPathError):
        file_system.addContentToFile("/b/log.txt", "Content#1")


def test_add_content_to_file_throw_exception_if_path_is_directory():
    file_system = FileSystem()
    file_system.mkdir("/a/b")
    with pytest.raises(PermissionError):
        file_system.addContentToFile("/a/b", "Content#1")


def test_add_content_to_file_throw_exception_if_file_is_binary():
    file_system = FileSystem()
    file_system.mkdir("/a")
    file_system.createBinaryFile("/a/file.bin", "Binary content")
    with pytest.raises(PermissionError):
        file_system.addContentToFile("/a/file.bin", "Content#1")


def test_add_content_to_file_success():
    file_system = FileSystem()
    file_system.mkdir("/a")
    file_system.createFile("/a/log.txt")
    file_system.createBufferFile("/a/file.buff")
    file_system.addContentToFile("/a/log.txt", "Log#1")
    file_system.addContentToFile("/a/log.txt", "Log#2")
    file_system.addContentToFile("/a/file.buff", "Log#1")
    file_system.addContentToFile("/a/file.buff", "Log#2")
    assert file_system.readContentFromFile("/a/log.txt") == "Log#1Log#2"
    assert file_system.readContentFromFile("/a/file.buff") == "Log#1"
    assert file_system.readContentFromFile("/a/file.buff") == "Log#2"

