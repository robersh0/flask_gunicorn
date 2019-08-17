import logging
import os
import sys
from flask_log_request_id import RequestIDLogFilter


logger = logging.getLogger('app')

level = logging.getLevelName(os.environ.get('BACKEND_LOGLEVEL', 'INFO').upper())

console_formatter = logging.Formatter("[backend] [%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - "
                                      "request_id=%(request_id)s - %(message)s")


console = logging.StreamHandler(stream=sys.stdout)
console.addFilter(RequestIDLogFilter())
console.setFormatter(console_formatter)
logger.addHandler(console)
logger.setLevel(level)

logger.info('Logger set with level %s' % logging.getLevelName(level))
