from src.config.general import RESPONSES
from flask import jsonify


def get_response(tag):
    return RESPONSES[tag]


def send(tag):
    response = get_response(tag)
    return jsonify(response), int(response['code'])


def send_post_response(id):
    response = get_response('POST_SUCCESS')
    response['id'] = id
    return jsonify(response), int(response['code'])


def send_post_response_results(results):
    response = get_response('POST_SUCCESS')
    response['results'] = results
    return jsonify(response), int(response['code'])


def send_post_response_id_results(id, results):
    response = get_response('POST_SUCCESS_ADDED')
    response['id'] = str(id)
    response['results'] = results
    return jsonify(response), int(response['code'])
