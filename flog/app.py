import click
from flask import Flask
from flask.cli import FlaskGroup
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    # Circular imports require this import to go inside the function
    from flog import views

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'postgresql://postgres:password@localhost:54321/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(views.public)

    return app


@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    """Management script for the Wiki application."""
