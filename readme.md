# Flog

# Install & Run Tests

```
$ pip install -r requirements.txt
$ pip install -e .
$ pytest
```

# App & Test Setup

* PostgreSQL: `docker-compose up -d` or use your own server
* Dependencies (see `requirements.txt`)
* [Flask App Factory Pattern](https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/)
* [Flask CLI: Custom Scripts](https://flask.palletsprojects.com/en/1.1.x/cli/#custom-scripts)
* [Pytest Fixtures](https://docs.pytest.org/en/latest/fixture.html)


# 2/27/20

```
$ ab -t 5 -c 5 http://localhost:5000/

$ waitress-serve --port=5000 server_falcon:falcon_app
$ waitress-serve --port=5000 server_flask:flask_app

$ gunicorn -b 127.0.0.1:5000 --workers=5 --worker-class=meinheld.gmeinheld.MeinheldWorker server_falcon:falcon_app
$ gunicorn -b 127.0.0.1:5000 --workers=5 --worker-class=meinheld.gmeinheld.MeinheldWorker server_flask:flask_app
```
