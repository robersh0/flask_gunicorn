import traceback

from flask import jsonify
from src.config.general import ERRORS
from src.tools.logger import logger
from src.tools.exceptions.base import GunicornFlaskBaseException


def get_error(tag):
    return ERRORS[tag]


def get_error_with_exception(exception):
    return exception.serialize


def get_array_error(code):
    return {
        'error': code
    }


def send_error(exception):
    if isinstance(exception, GunicornFlaskBaseException):
        error = get_error_with_exception(exception)
        logger.exception(exception)
        return jsonify(error), int(error['code'])

    trace = traceback.format_exc()
    exception = GunicornFlaskBaseException(tag='INTERNAL_ERROR', trace=trace)
    error = get_error_with_exception(exception)
    logger.exception(exception)
    return jsonify(error), int(error['code'])
