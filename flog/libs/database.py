from sqlalchemy_utils import functions as safunc


def create_db(db_url, replace_existing):
    if replace_existing and safunc.database_exists(db_url):
        safunc.drop_database(db_url)

    safunc.create_database(db_url)
