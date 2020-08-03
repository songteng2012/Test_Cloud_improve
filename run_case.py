import unittest
from utils.path_config import TEST_PATH



if __name__ == '__main__':
    discover = unittest.defaultTestLoader.discover(TEST_PATH, pattern='*.py')
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(discover)
