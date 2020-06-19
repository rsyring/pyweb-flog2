import os

db_uri = 'postgresql://postgres@localhost:54321/flog'


def development_config(app, config):
    config['SQLALCHEMY_DATABASE_URI'] = db_uri

    return config


def testing_config(app, config):
    if 'CI' in os.environ:
        config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost/postgres'
    else:
        config['SQLALCHEMY_DATABASE_URI'] = db_uri + '_tests'

    return config
