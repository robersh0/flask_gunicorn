import os

POSTGRES = {
    'user': os.getenv('POSTGRES_USER'),
    'pw': os.getenv('POSTGRES_PASSWORD'),
    'db': os.getenv('POSTGRES_DB'),
    'host': os.getenv('POSTGRES_HOST'),
    'port': os.getenv('POSTGRES_PORT'),
}

# General configuration
CONFIG = {
    'database': {
        'uri': 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    },
    'sentry': {
        'config': {
            'release': '0.1.0'
        },
        'dsn': os.getenv('SENTRY_DSN')
    },
    'app': {
        'port': os.getenv('PUBLIC_PORT'),
        'root': os.getenv('ROOT_PATH')
    }
}

RESPONSES = {
    'RESOURCE_DELETED': {
        'code': 200,
        'message': 'Resource deleted',
    },
    'RESOURCE_UPDATED': {
        'code': 200,
        'message': 'Resource updated',
    },
    'POST_SUCCESS_ADDED': {
        'code': 201,
        'message': 'Resource added',
    },
    'POST_SUCCESS': {
        'code': 200,
        'message': 'Resource not saved',
    }
}

ERRORS = {
    'RESOURCE_NOT_FOUND': {
        'internal_code': 'E0003',
        'code': 404,
        'message': 'resource not found',
    },
    'MALFORMED_REQUEST': {
        'internal_code': 'E0004',
        'code': 400,
        'message': 'Malformed request',
    },
    'INTERNAL_ERROR': {
        'internal_code': 'E0001',
        'code': 503,
        'message': 'Internal error',
    },
    'UNAUTHORIZED': {
        'internal_code': 'E0008',
        'code': 401,
        'message': 'UNAUTHORIZED',
    },
    'FORBIDDEN': {
        'internal_code': 'E0009',
        'code': 403,
        'message': 'FORBIDDEN',
    },
    'DECODE_ERROR': {
        'internal_code': 'E0010',
        'code': 401,
        'message': 'UNAUTHORIZED',
    },
    'ENCODE_ERROR': {
        'internal_code': 'E0011',
        'code': 503,
        'message': 'Internal error',
    },
    'NO_USER': {
        'internal_code': 'E0012',
        'code': 503,
        'message': 'Internal error',
    },
    'CONFLICT': {
        'internal_code': 'E0016',
        'code': 409,
        'message': 'CONFLICT',
    }
}
