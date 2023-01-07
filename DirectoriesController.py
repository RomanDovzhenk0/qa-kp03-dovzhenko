from flask import request, abort
from flask_restful import Resource

from FileSystemService import service
from InvalidPathError import InvalidPathError


class DirectoriesController(Resource):
    def get(self):
        path = request.args.get('path', default='/', type=str)
        try:
            return service.ls(path)
        except InvalidPathError as err:
            abort(400, err)

    def post(self):
        path = request.args.get('path', default='/', type=str)
        try:
            service.mkdir(path)
            return '', 201
        except InvalidPathError as err:
            abort(400, err)

    def put(self):
        path = request.args.get('path', default='/', type=str)
        newPath = request.args.get('newPath', default='/', type=str)
        try:
            service.move_node(path, newPath)
            return '', 200
        except InvalidPathError as err:
            abort(400, err)

    def delete(self):
        path = request.args.get('path', default='/', type=str)
        try:
            service.delete_node(path)
            return '', 200
        except InvalidPathError as err:
            abort(400, err)
