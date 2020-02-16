import sys
import pandas as pd
from flask import Flask, request, jsonify
from flask_rest_api import Blueprint
from commons import db_manager as ut, Logger
from flask_restplus import reqparse
parser = reqparse.RequestParser()

logger = Logger.get_logger("CrediWatch")
from flask import send_file
from flask_restplus import Namespace, Resource, fields
from flask import Flask, render_template
from werkzeug.datastructures import FileStorage
import commons.db_manager as db_mgr

db_mgr = db_mgr.DataConnectionManager()
db_mgr.get_connection()

data_ingestion_api = Namespace('DataIngestion', description="REST services related to Data Ingestion")


upload_parser = data_ingestion_api.parser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)


@data_ingestion_api.route("/ingestFileData")
class Ingest(Resource):
    @data_ingestion_api.expect(upload_parser)
    def post(self):
        args = upload_parser.parse_args()
        df = pd.read_csv(args['file'])
        data_dct = None

        try:
            data_dct = df.to_dict(orient="records")
        except Exception as e:
            logger.error("Error in extraction of data from file: {}".format(str(e)))

        # code to insert data to Mongo DB
        if data_dct is not None:
            status = db_mgr.insert_data(data_dct)
            status_msg = {"Message": status}
        else:
            status_msg = {"Message": "Couldnt insert data"}

        return jsonify(status_msg)


@data_ingestion_api.route("/ingestFileData")
class Analyse(Resource):
    @data_ingestion_api.expect(upload_parser)
    def post(self):
        args = upload_parser.parse_args()
        df = pd.read_csv(args['file'])
        data_dct = None

        try:
            data_dct = df.to_dict(orient="records")
        except Exception as e:
            logger.error("Error in extraction of data from file: {}".format(str(e)))

        # code to insert data to Mongo DB
        if data_dct is not None:
            status = db_mgr.insert_data(data_dct)
            status_msg = {"Message": status}
        else:
            status_msg = {"Message": "Couldnt insert data"}

        return jsonify(status_msg)