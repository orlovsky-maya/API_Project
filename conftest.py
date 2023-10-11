import pytest
from utils.logger import Logger


@pytest.fixture(scope='function')
def logger(request):
    logger = Logger(request.config.rootdir)
    return logger
