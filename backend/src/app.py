import traceback
import pickle
from flask_migrate import Migrate
from flask import Flask, request
from src.tools.logger import logger
from src.tools import error_handler
from src.config.general import CONFIG
from src.models.database import database
from src.blueprints.health import health_check
from src.blueprints.predict import predict_endpoint
from src.tools.exceptions.base import GunicornFlaskBaseException
from flask_log_request_id import RequestID

app = Flask(__name__)
RequestID(app)

with app.app_context():
    # configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = CONFIG['database']['uri']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SENTRY_CONFIG'] = CONFIG['sentry']['config']
    app.config['APPLICATION_ROOT'] = CONFIG['app']['root']

    # Force to use our own logger
    app.logger = logger

    with open('model.pickle', 'rb') as handle:
        app.model = pickle.load(handle)

    # create database
    database.init_app(app)
    database.create_all(bind=None)

    # Migrate
    migrate = Migrate(app, database)

    # Routes
    app.register_blueprint(health_check, url_prefix=CONFIG['app']['root'])
    app.register_blueprint(predict_endpoint, url_prefix=CONFIG['app']['root'])

    @app.after_request
    def after_request(response):
        """ Logging after every request. """
        if response.status_code != 500:
            logger.info('%s %s %s %s %s',
                        request.remote_addr,
                        request.method,
                        request.scheme,
                        request.full_path,
                        response.status)
        return response

    @app.errorhandler(GunicornFlaskBaseException)
    def exceptions_insights_base(exception):
        return error_handler.send_error(exception=exception)

    @app.errorhandler(Exception)
    def exceptions(e):
        """ Logging after every Exception. """
        tb = traceback.format_exc()
        logger.error(msg=tb)
        if "404" in str(e):
            return "Not found", 404
        return "Internal Server Error", 500


if __name__ == "__main__":
    print("hello!!")
    print(int(CONFIG['app']['port']))
    app.run(host="0.0.0.0", threaded=True, port=int(CONFIG['app']['port']), debug=False)
