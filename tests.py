# tests/test_curves.py

import unittest
import numpy as np
from src.curves import read_csv

class TestCurves(unittest.TestCase):
    def test_read_csv(self):
        path_XYs = read_csv('data/examples/isolated.csv')
        self.assertIsInstance(path_XYs, list)

if __name__ == '__main__':
    unittest.main()

# Similar tests can be created for other modules
