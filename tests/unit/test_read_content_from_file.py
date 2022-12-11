import pytest

from exceptions import InvalidPathError
from main import FileSystem


def test_read_content_from_file_throw_exception_if_file_path_invalid():
    file_system = FileSystem()
    file_system.mkdir("/a")
    file_system.create_file("/a/log.txt")
    with pytest.raises(InvalidPathError):
        file_system.read_content_from_file("/b/log.txt")


def test_read_content_from_file_throw_exception_if_file_path_is_directory():
    file_system = FileSystem()
    file_system.mkdir("/a")
    with pytest.raises(PermissionError):
        file_system.read_content_from_file("/a")


def test_read_content_from_file_success_if_file_is_binary_or_log():
    file_system = FileSystem()
    file_system.mkdir("/a")
    file_system.create_file("/a/log.txt")
    file_system.add_content_to_file("/a/log.txt", "Log content")
    file_system.create_binary_file("/a/file.bin", "Binary content")
    assert file_system.read_content_from_file("/a/log.txt") == "Log content"
    assert file_system.read_content_from_file("/a/file.bin") == "Binary content"


def test_read_content_from_file_success_if_file_is_buffer():
    file_system = FileSystem()
    file_system.mkdir("/a")
    file_system.create_buffer_file("/a/file.buff")
    file_system.add_content_to_file("/a/file.buff", "data-1")
    file_system.add_content_to_file("/a/file.buff", "data-2")
    file_system.add_content_to_file("/a/file.buff", "data-3")
    assert file_system.read_content_from_file("/a/file.buff") == "data-1"
    assert file_system.read_content_from_file("/a/file.buff") == "data-2"
    assert file_system.read_content_from_file("/a/file.buff") == "data-3"
