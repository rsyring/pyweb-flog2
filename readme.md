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
