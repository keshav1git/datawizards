from flask import Flask, jsonify
from flask_restplus import Resource
from apis import api
import datetime
from flask_cors import CORS
flask_app = Flask(__name__)


@api.route("/status")
class health(Resource):
    def get(self):
        return jsonify({
            "status": "running",
            "datetime": str(datetime.datetime.now())})


if __name__ == "__main__":

    api.init_app(flask_app)
    CORS(flask_app)
    flask_app.run(debug=True)
