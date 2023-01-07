import os

from FileAlreadyExistError import FileAlreadyExistError
from InvalidPathError import InvalidPathError
from TrieNode import TrieNode


class FileSystemService:

    def __init__(self):

        self.__root = TrieNode()

    def mkdir(self, path):
        if not path.startswith("/"):
            raise InvalidPathError("Invalid path: " + path)
        parts = path.split("/")
        parts.pop(0)
        for part in parts:
            if part == '':
                raise InvalidPathError("Invalid path: " + path)
        buffer = ""
        for s in self.__split(path, '/'):
            buffer += "/" + s
            try:
                node = self.__get_node(buffer)
            except InvalidPathError:
                break
            if node.is_file:
                raise InvalidPathError("Invalid path: " + path)
        curr = self.__put_node(path)
        curr.is_file = False

    def delete_node(self, path):
        self.__get_node(path)
        curr = self.__root
        for s in self.__split(path, '/')[:-1]:
            curr = curr.children[s]

        del curr.children[self.__split(path, '/')[-1]]

    def ls(self, path):

        curr = self.__get_node(path)
        if curr.is_file:
            return [self.__split(path, '/')[-1]]

        return sorted(curr.children.keys())

    def move_node(self, old_path, new_path):
        self.__get_node(old_path)
        self.__get_node(new_path)
        if new_path.startswith(old_path):
            raise InvalidPathError("Unable to move directory " + old_path + " to " + new_path)
        curr = self.__root
        for s in self.__split(old_path, '/'):
            curr = curr.children[s]

        puth = self.__root
        for i in self.__split(new_path, '/'):
            puth = puth.children[i]

        puth.children[s] = curr
        self.delete_node(old_path)

    def create_binary_file(self, file_path, content):
        head, tail = os.path.split(file_path)
        self.__get_node(head)
        try:
            self.__get_node(file_path)
            raise FileAlreadyExistError("File " + tail + " in path:" + head + " already exists")
        except InvalidPathError:
            curr = self.__put_node(file_path)
            curr.is_file = True
            curr.content += content
            curr.is_binary = True

    def read_content_from_file(self, file_path):
        curr = self.__get_node(file_path)
        if not curr.is_file:
            raise PermissionError("Unable to read content from directory")
        if curr.is_buffer:
            try:
                return curr.queue.pop()
            except IndexError:
                return ''
        return curr.content

    def create_file(self, file_path):
        head, tail = os.path.split(file_path)
        self.__get_node(head)
        try:
            self.__get_node(file_path)
            raise FileAlreadyExistError("File " + tail + " in path:" + head + " already exists")
        except InvalidPathError:
            curr = self.__put_node(file_path)
            curr.is_file = True

    def create_buffer_file(self, file_path):
        head, tail = os.path.split(file_path)
        self.__get_node(head)
        try:
            self.__get_node(file_path)
            raise FileAlreadyExistError("File " + tail + " in path:" + head + " already exists")
        except InvalidPathError:
            curr = self.__put_node(file_path)
            curr.is_file = True
            curr.is_buffer = True

    def add_content_to_file(self, file_path, content):
        curr = self.__get_node(file_path)

        if curr.is_binary:
            raise PermissionError("Unable to add content to immutable file")
        elif curr.is_buffer:
            curr.queue.append(content)
        elif curr.is_file:
            curr.content += content
        else:
            raise PermissionError("Unable to add content to directory")

    def __get_node(self, path):
        is_invalid_file_path = False
        try:
            curr = self.__root
            for s in self.__split(path, '/'):
                curr = curr.children[s]
            return curr
        except KeyError:
            is_invalid_file_path = True
        if is_invalid_file_path:
            raise InvalidPathError("Path does not exist: " + path)

    def __put_node(self, path):
        curr = self.__root

        for s in self.__split(path, '/'):
            if s not in curr.children:
                if curr.is_file:
                    break
                curr.children[s] = TrieNode()
            curr = curr.children[s]

        return curr

    def __split(self, path, delim):
        if path == '/':
            return []
        return path.split('/')[1:]


service = FileSystemService()
