Flog
====

[![CircleCI](https://circleci.com/gh/rsyring/pyweb-flog2.svg?style=svg)](https://circleci.com/gh/rsyring/pyweb-flog2)
[![codecov](https://codecov.io/gh/rsyring/pyweb-flog2/branch/master/graph/badge.svg)](https://codecov.io/gh/rsyring/pyweb-flog2)



Run Tests
----------------------------------

```
# first
$ docker-compose up -d

# then
$ tox

# or (this is also how to get a dev environment setup)
$ pip install -r requirements.txt
$ pip install -e .
$ pytest
```

Features
--------

- General
    - ease of starting tests & dev
    - docker-compose
    - freeze requirements using pip-tools
        - tox runs both frozen and current libs
- App factory pattern
    - blueprints (web & CLI)
    - use .ext module to avoid circular imports
- CLI Integration
    - custom command
    - two-phase init for blueprints
- Configuration
    - .env & .flaskenv
    - from files
    - from environment
    - alternate settings for testing, dev, prod
    - init config first or logging first?
- Logging
    - logs are probably cheap, don't prematurely optimize
    - centralize your logs to an aggregation service
    - .info logs are show/saved by default
    - cli output is plain text
    - saved logs are JSON
    - saved logs go to syslog, let devops handle the aggregation
- Testing
    - alternate DB URI
    - pytest & fixtures
    - custom pytest.ini for tox/ci
- Flask-SQLAlchemy
    - ext init
    - fixtures to get db to ensure app context
- Celery
    - refresh process pool
