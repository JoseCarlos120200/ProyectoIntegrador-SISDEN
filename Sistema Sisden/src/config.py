class Config:
    SECRET_KEY = 'root'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'clinica'


config = {
    'development': DevelopmentConfig
}
