import pytest

import flog.app
import flog.ext


@pytest.fixture(scope='session')
def app():
    app = flog.app.FlogApp.create(testing=True)

    flog.ext.db.drop_all(app=app)
    flog.ext.db.create_all(app=app)

    return app


@pytest.fixture()
def db(app):
    # print('db fixture')
    with app.app_context():
        yield flog.ext.db
        flog.ext.db.session.remove()


@pytest.fixture()
def web(app):
    return app.test_client()


@pytest.fixture()
def cli(app):
    return app.test_cli_runner()


@pytest.fixture(scope='session')
def script_args():
    return ['python', '-c', 'from flog import app; app.cli()']
