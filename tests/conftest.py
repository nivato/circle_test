import logging
import pytest

from types import SimpleNamespace


logger = logging.getLogger(__name__)
common_context = SimpleNamespace()


@pytest.fixture
def context():
    return common_context


def pytest_configure(config):
    suppressed_loggers = ['faker.factory', 'urllib3.connectionpool', 'open_publishing.gjp']
    for log_name in suppressed_loggers:
        logging.getLogger(log_name).setLevel(logging.CRITICAL)


def pytest_sessionstart(session):
    logger.info('Started running tests')


def pytest_runtest_setup(item):
    logger.info(f'TEST START: {item.nodeid}')


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """ a hook to get test report and log errors to the log file in case of test failures """
    outcome = yield
    report = outcome.get_result()

    # we only look at actual failing test calls, not setup/teardown
    if report.when == 'call' and report.failed:
        logger.error(report.longreprtext)


def pytest_runtest_teardown(item, nextitem):
    logger.info(f'TEST END: {item.nodeid}')


def pytest_sessionfinish(session, exitstatus):
    logger.info('Finished running tests')
    logger.info(f'Exit status: {exitstatus}')
    logger.info(f'Context: {common_context}')
