import logging


logger = logging.getLogger(__name__)


class TestSomethingWorks(object):

    def test_one(self):
        logger.info('First test started')
        x = "this"
        assert 'h' in x

    def test_two(self):
        logger.info('Second test started')
        x = "hello"
        assert hasattr(x, 'join')
