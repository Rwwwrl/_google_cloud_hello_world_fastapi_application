from src.settings import settings


def test_env_variable():
    assert settings.MY_SECRET_VALUE == "FROM TESTS ENV"
