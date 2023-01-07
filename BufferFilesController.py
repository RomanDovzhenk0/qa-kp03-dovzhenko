from flask import request, abort
from flask_restful import Resource

from FileAlreadyExistError import FileAlreadyExistError
from FileSystemService import service
from InvalidPathError import InvalidPathError


class BufferFilesController(Resource):
    def get(self):
        path = request.args.get('path', default='/', type=str)
        try:
            return service.read_content_from_file(path)
        except InvalidPathError as err:
            abort(400, err)
        except PermissionError as err:
            abort(400, err)

    def post(self):
        path = request.args.get('path', default='/', type=str)
        try:
            service.create_buffer_file(path)
            return '', 201
        except InvalidPathError as err:
            abort(400, err)
        except FileAlreadyExistError as err:
            abort(400, err)

    def put(self):
        path = request.args.get('path', default='/', type=str)
        content = request.args.get('content', default='/', type=str)
        try:
            service.add_content_to_file(path, content)
            return '', 200
        except InvalidPathError as err:
            abort(400, err)
        except PermissionError as err:
            abort(400, err)

    def delete(self):
        path = request.args.get('path', default='/', type=str)
        try:
            service.delete_node(path)
            return '', 200
        except InvalidPathError as err:
            abort(400, err)
