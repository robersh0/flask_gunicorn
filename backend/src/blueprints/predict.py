import logging

from flask import Blueprint, request
from flask import current_app as app
from sqlalchemy.exc import IntegrityError, DataError

from src.models.database import database
from src.models.prediction import Prediction
from src.tools import predict
from src.tools import response_handler
from src.tools.exceptions.predict import PredictException

logger = logging.getLogger('app')
predict_endpoint = Blueprint('predict_endpoint', __name__, template_folder='blueprints')


@predict_endpoint.route('/score', methods=['POST'])
def score():
    file = request.files.get('file')
    results = predict.make_prediction(app.model, file.read())

    return response_handler.send_post_response_results(results=results)


@predict_endpoint.route('/score_save', methods=['POST'])
def score_and_save():
    file = request.files.get('file')
    results = predict.make_prediction(app.model, file.read())

    json_data = {
        'file_name': file.filename,
        'model_name': "test",
        'model_path': "test",
        'results': str(results)
    }

    try:
        prediction = Prediction(json=json_data)
        database.session.add(prediction)
        database.session.commit()
        return response_handler.send_post_response_id_results(id=prediction.serialize['id'],
                                                              results=results)
    except DataError:
        raise PredictException('MALFORMED')
    except IntegrityError:
        raise PredictException('CONFLICT')
