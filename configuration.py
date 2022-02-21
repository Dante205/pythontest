class BaseConfig(object):
    'Base configuracion'
    SECRET_KEY = "change-this-key-in-the-application-config"
    JWT_SECRET_KEY = "change-this-key-to-something-different-in-the-application-config"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:root@localhost:3306/prueba"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    # # SQLite
    # sqlite:///database.db
    # # MySQL
    # mysql+pymysql://user:password@ip:port/db_name
    # # Postgres
    # postgresql+psycopg2://user:password@ip:port/db_name
    # # MSSQL
    # mssql+pyodbc://user:password@dns_name
    # # Oracle
    # oracle+cx_oracle://user:password@ip:port/db_name

    #WTF_CSRF_TIME_LIMIT = 10


class ProductionConfig(BaseConfig):
    'Produccion configuracion'
    DEBUG = False
    SECRET_KEY = 'Produccion key'


class DevelopmentConfig(BaseConfig):
    'Desarrollo configuracion'
    DEBUG = True
    SECRET_KEY = 'Desarrollo key'