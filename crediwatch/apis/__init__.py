from flask_restplus import Api

from services.data_ingestion import data_ingestion_api as data_ingestion_namespace
from services.insights import insights_api as insights_api_namespace

api = Api(
    title='CrediWatch',
    version='1.0',
    description='REST API Framework for CrediWatch',

)

api.add_namespace(data_ingestion_namespace)
api.add_namespace(insights_api_namespace)
