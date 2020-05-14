import logging


logger = logging.getLogger(__name__)


def pytest_configure(config):
    suppressed_loggers = ['faker.factory', 'urllib3.connectionpool', 'open_publishing.gjp']
    for log_name in suppressed_loggers:
        logging.getLogger(log_name).setLevel(logging.CRITICAL)


def pytest_runtest_setup(item):
    logger.info(f'pytest_runtest_setup [name] {item.name}')


def pytest_runtest_call(item):
    logger.info(f'pytest_runtest_call [name] {item.name}')


def pytest_runtest_teardown(item, nextitem):
    logger.info(f'pytest_runtest_teardown [name] {item.name}')
