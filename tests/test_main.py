import unittest
import sys
import os

# Add the src directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import main


class TestMain(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(main.hello(), '10 Academy week 0 challenge starter code')

if __name__ == '__main__':
    unittest.main()