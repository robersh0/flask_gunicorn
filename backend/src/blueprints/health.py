from flask import Blueprint, jsonify
health_check = Blueprint('health_check', __name__, template_folder='blueprints')


@health_check.route('/health')
def health_check_endpoint():
    version = {'version': '1.0.0'}

    return jsonify(version)
