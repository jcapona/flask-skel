import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    LOG_FILE = os.environ.get("LOG_PATH")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    PROD = True


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


def get_config(key):
    config_dict = {
        "prod": ProductionConfig,
        "dev": DevelopmentConfig,
        "test": TestingConfig
    }

    key = key if key in config_dict else "dev"
    return config_dict[key]
