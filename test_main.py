# -*- coding: utf-8 -*-
from main import quadratic, second_eig, power_iter
import unittest
import numpy as np

class TestCase(unittest.TestCase):

    def assertAllClose(self, a, b):
        self.assertTrue(np.allclose(a, b))

    def test_quadratic(self):
        self.assertAllClose(float(quadratic(np.identity(10), np.ones(10))),
                            np.sqrt(10))
        self.assertAllClose(float(quadratic(np.array([[2, 1], [1, 2]]), np.array([0.1, 0.5]))),
                            0.3741657386773941)

    def test_second_eig(self):
        self.assertAllClose(second_eig(np.identity(10)), 1.0)
        self.assertAllClose(second_eig(np.array([[2., 0.], [0., 1.]])), 1.0)

    def test_power_iter(self):
        self.assertAllClose(power_iter(np.identity(10),
                                       np.ones(10),
                                       100),
                            1.0)
        self.assertAllClose(power_iter(np.array([[2, 1], [1, 2]]),
                                       np.array([1, 2]),
                                       100),
                            3.0)
        self.assertAllClose(power_iter(np.array([[5, -1], [-1, 5]]),
                                       np.array([0., 1.]),
                                       100),
                            6.0)
        

if __name__ == "__main__":
    unittest.main()
