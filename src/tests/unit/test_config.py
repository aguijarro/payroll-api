import os


def test_development_config(test_app):
    test_app.config.from_object('src.config.DevelopmentConfig')
    assert test_app.config['SECRET_KEY'] == 'tempo'
    assert not test_app.config['TESTING']


def test_testing_config(test_app):
    test_app.config.from_object('src.config.TestingConfig')
    assert test_app.config['SECRET_KEY'] == 'tempo'
    assert test_app.config['TESTING']
    assert not test_app.config['PRESERVE_CONTEXT_ON_EXCEPTION']


def test_production_config(test_app):
    test_app.config.from_object('src.config.ProductionConfig')
    assert test_app.config['SECRET_KEY'] == 'tempo'
    assert not test_app.config['TESTING']
