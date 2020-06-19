Flog
====

Install Dependencies & Run Tests
----------------------------------

```
$ docker-compose up -d
$ pip install -r requirements.txt
$ pytest
```

Features
--------

- General
    - requirements
    - docker-compose
    - tox & CI
    - ease of starting tests & dev
- App factory pattern
    - blueprints (web & CLI)
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
- Flask-SQLAlchemy
    - ext init
    - fixtures to get db to ensure app context
- Celery
    - refresh process pool
