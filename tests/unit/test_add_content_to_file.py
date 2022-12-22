import pytest

from Exceptions.exceptions import InvalidPathError
from Application.Service.FileSystemService import FileSystemService


def test_add_content_to_file_throw_exception_if_file_path_invalid():
    file_system = FileSystemService()
    file_system.mkdir("/a")
    file_system.create_file("/a/log.txt")
    with pytest.raises(InvalidPathError):
        file_system.add_content_to_file("/b/log.txt", "Content#1")


def test_add_content_to_file_throw_exception_if_path_is_directory():
    file_system = FileSystemService()
    file_system.mkdir("/a/b")
    with pytest.raises(PermissionError):
        file_system.add_content_to_file("/a/b", "Content#1")


def test_add_content_to_file_throw_exception_if_file_is_binary():
    file_system = FileSystemService()
    file_system.mkdir("/a")
    file_system.create_binary_file("/a/file.bin", "Binary content")
    with pytest.raises(PermissionError):
        file_system.add_content_to_file("/a/file.bin", "Content#1")


def test_add_content_to_file_success():
    file_system = FileSystemService()
    file_system.mkdir("/a")
    file_system.create_file("/a/log.txt")
    file_system.create_buffer_file("/a/file.buff")
    file_system.add_content_to_file("/a/log.txt", "Log#1")
    file_system.add_content_to_file("/a/log.txt", "Log#2")
    file_system.add_content_to_file("/a/file.buff", "Log#1")
    file_system.add_content_to_file("/a/file.buff", "Log#2")
    assert file_system.read_content_from_file("/a/log.txt") == "Log#1Log#2"
    assert file_system.read_content_from_file("/a/file.buff") == "Log#1"
    assert file_system.read_content_from_file("/a/file.buff") == "Log#2"
