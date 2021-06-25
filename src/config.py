class BaseConfig:
    TESTING = False
    SECRET_KEY = 'tempo'


class DevelopmentConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    TESTING = True


class ProductionConfig(BaseConfig):
    pass
