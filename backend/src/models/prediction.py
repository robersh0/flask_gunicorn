from sqlalchemy import text as sa_text
from .database import database
from src.tools.exceptions.predict import PredictException
from datetime import datetime


class Prediction(database.Model):
    __tablename__ = 'prediction'

    id = database.Column(database.BigInteger, primary_key=True, autoincrement=True)
    file_name = database.Column(database.String(75), unique=False, nullable=False)
    model_name = database.Column(database.String(75), unique=False, nullable=False)
    model_path = database.Column(database.String(75), unique=False, nullable=False)
    results = database.Column(database.Text(), unique=False, nullable=False)
    creation_date = database.Column(database.DateTime, unique=False, nullable=False,
                                    server_default=sa_text("date '2019-08-01'"))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'file_name': self.file_name,
            'model_name': self.model_name,
            'model_path': self.model_path,
            'results': self.results,
            'creation_date': self.creation_date
        }

    @property
    def serialize_without_sensitive_data(self):
        return {
            'id': self.id,
            'file_name': self.file_name,
            'creation_date': self.creation_date
        }

    @staticmethod
    def check_data(object_json):
        if 'file_name' not in object_json:
            return False
        if 'model_name' not in object_json:
            return False
        if 'model_path' not in object_json:
            return False
        if 'results' not in object_json:
            return False
        return True

    def __init__(self, json):
        if self.check_data(json):
            self.file_name = json['file_name']
            self.model_name = json['model_name']
            self.model_path = json['model_path']
            self.results = json['results']
            self.creation_date = datetime.now()
        else:
            raise PredictException('MALFORMED')

    def __repr__(self):
        return 'ID %s and file_name %s.' % (self.id, self.file_name)
