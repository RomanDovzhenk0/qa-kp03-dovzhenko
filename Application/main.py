from flask import Flask
from flask_restful import Api

from Infrastructure.Rest.BinaryFilesController import BinaryFilesController
from Infrastructure.Rest.BufferFilesController import BufferFilesController
from Infrastructure.Rest.DirectoriesController import DirectoriesController
from Infrastructure.Rest.LogTextFilesController import LogTextFilesController

app = Flask(__name__)
api = Api(app)
api.add_resource(BinaryFilesController, '/binaryfiles')
api.add_resource(BufferFilesController, '/bufferfiles')
api.add_resource(LogTextFilesController, '/logtextfiles')
api.add_resource(DirectoriesController, '/directories')

if __name__ == '__main__':
    app.run()
