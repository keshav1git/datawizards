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

insights_api = Namespace('Insights', description="REST services related to Data Insights")

score_model = insights_api.model("Insights", {
    "CIN": fields.String("CIN")
})


@insights_api.route("/analyse")
class Insights(Resource):
    @insights_api.expect(score_model)
    def post(self):
        data = request.get_json()
        if data is not None:
            try:
                CIN = data["CIN"]
                data = db_mgr.analyse_data(CIN)
            except Exception as e:
                logger.error("Error Occurred {}".format(str(e)))
        else:
            data = "None"
        return jsonify({"data": data})
