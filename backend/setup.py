from setuptools import setup, find_packages

dependencies = [
    'gunicorn==19.9.0',
    'Flask==1.0.2',
    'flask-sqlalchemy==2.3.2',
    'psycopg2-binary',
    'requests',
    'sqlalchemy',
    'pandas==0.23.0',
    'flask_log_request_id',
    'Flask-Migrate',
    'flake8',
    'scikit-learn==0.19.2',
    'scipy==1.0.0'
]

dev_dependencies = [
]

setup(
    name='app',
    version='1.0.0',
    description='Flask Gunicorn app',
    url='https://github.com/robersh0/flask_gunicorn.git',
    packages=find_packages(exclude=['*tests']),
    include_package_data=True,
    install_requires=dependencies,
    extras_require={
        'dev': dev_dependencies
    }
)
