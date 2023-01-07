from flask import Flask
from flask_restful import Api

from BinaryFilesController import BinaryFilesController
from BufferFilesController import BufferFilesController
from DirectoriesController import DirectoriesController
from LogTextFilesController import LogTextFilesController

app = Flask(__name__)
api = Api(app)
api.add_resource(BinaryFilesController, '/binaryfiles')
api.add_resource(BufferFilesController, '/bufferfiles')
api.add_resource(LogTextFilesController, '/logtextfiles')
api.add_resource(DirectoriesController, '/directories')

if __name__ == '__main__':
    app.run(port=5000)
