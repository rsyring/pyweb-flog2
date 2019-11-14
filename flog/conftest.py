from mixer.backend.flask import mixer as flask_mixer
import pytest

import flog.app


@pytest.fixture(scope='session')
def app():
    app = flog.app.create_app()
    app.testing = True

    flog.app.db.drop_all(app=app)
    flog.app.db.create_all(app=app)

    return app


@pytest.fixture()
def db(app):
    # print('db fixture')
    with app.app_context():
        yield flog.app.db
        flog.app.db.session.remove()


@pytest.fixture(scope='session')
def mixer_ext(app):
    # print('mixer_ext fixture')
    mixer = flask_mixer
    mixer.init_app(app)
    return mixer


@pytest.fixture()
def mixer(mixer_ext, db):
    # print('mixer fixture')
    return flask_mixer


@pytest.fixture()
def client(app):
    return app.test_client()
