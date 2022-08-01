import os


class Config:
    JWT_SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class SqlLiteConfig(Config):
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' +\
        os.path.join(basedir, 'database.db')


class PostgresSqlConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{0}:{1}@{2}/{3}'.format(
        'postgres',
        'admin',
        '127.0.0.1:5432',
        'text-to-sound')
