import logging


logger = logging.getLogger(__name__)


def setup_module(module):
    """ setup any state specific to the execution of the given module."""
    logger.info('SETUP MODULE')


def teardown_module(module):
    """ teardown any state that was previously setup with a setup_module
    method.
    """
    logger.info('TEARDOWN MODULE')


class TestSomethingDoesntWork(object):

    @classmethod
    def setup_class(cls):
        logger.info('SETUP CLASS')

    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        logger.info('TEARDOWN CLASS')

    def setup_method(self, method):
        """ setup any state tied to the execution of the given method in a
        class.  setup_method is invoked for every test method of a class.
        """
        logger.info('SETUP METHOD')

    def teardown_method(self, method):
        """ teardown any state that was previously setup with a setup_method
        call.
        """
        logger.info('TEARDOWN METHOD')

    def test_three(self):
        logger.info('First test started')
        x = "this"
        assert 't' in x

    def test_four(self):
        logger.info('Second test started')
        x = "hello"
        assert hasattr(x, 'join')
