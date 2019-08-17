import logging
import json

from src.tools.exceptions.predict import PredictException

logger = logging.getLogger('app')


def make_prediction(model, file):
    input_vectors = [list(elem['features'].values()) for elem in json.loads(file)]
    results = model.predict_proba(input_vectors)
    return json.dumps(results.tolist())


def read_file(file_obj):
    if file_obj is None:
        raise PredictException('MALFORMED')

    logger.debug(file_obj.content_type)
    if file_obj.content_type != "application/json":
        logger.warning("Mimetype error.")

    file = str(file_obj.read(), 'utf-8')
    return file
