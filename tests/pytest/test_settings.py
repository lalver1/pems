def test_runtime_environment_default(settings):
    assert settings.RUNTIME_ENVIRONMENT() == "local"


def test_runtime_environment__local(settings):
    settings.ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
    assert settings.RUNTIME_ENVIRONMENT() == "local"


def test_runtime_environment_dev(settings):
    settings.ALLOWED_HOSTS = ["*"]
    assert settings.RUNTIME_ENVIRONMENT() == "dev"
