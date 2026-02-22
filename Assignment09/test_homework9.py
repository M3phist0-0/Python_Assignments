import unittest
import numpy as np
from homework9 import Distributions, NumpyDistributions

class TestDistributions(unittest.TestCase):
    """"
    unittests for the Distributions class
    """

    def test_gen_norm_distro(self):
        """"
        tests normal distribution generation
        """
        dist = Distributions(dist='normal', mean=0, std=1, size=1000)
        self.assertEqual(dist.distribution, 'normal')
        self.assertAlmostEqual(len(dist.data), 1000)
        self.assertTrue(np.isclose(np.mean(dist.data), 0, atol=0.1))
        self.assertTrue(np.isclose(np.std(dist.data), 1, atol=0.1))


    def test_lognormal_distro(self):
        """"
        tests lognormal distribution generation
        """
        dist = Distributions('lognormal', mean=1, std=5, size=1000)
        self.assertEqual(dist.distribution, 'lognormal')
        self.assertEqual(len(dist.data), 1000)

    def test_laplace_distro(self):
        """"
        tests laplace distro generation
        """
        dist = Distributions('laplace', mean=2, std=1, size=1000)
        self.assertEqual(dist.distribution, 'laplace')
        self.assertEqual(len(dist.data), 1000)

    def test_invalid_distro(self):
        """"
        tests handling invalid distro types
        """
        with self.assertRaises(ValueError):
            Distributions('thisiswrong', mean=0, std=1, size=1000)

    def test_negative_std(self):
        """"
        tests invalid negative scale
        """
        with self.assertRaises(ValueError):
            dist = Distributions(dist='normal', mean=0, std=-1, size=1000)


class TestNumpyDistribution(unittest.TestCase):
    """"
    unittests for the NumpyDistribution class
    """
    def test_normal_distro(self):
        """"
        tests normal distribution generation using NumPy methods
        """
        dist = NumpyDistributions('normal', mean=0, std=1, size=1000)
        self.assertEqual(dist.distribution, 'normal')
        self.assertEqual(len(dist.data), 1000)
        self.assertTrue(np.isclose(np.mean(dist.data), 0, atol=0.1))
        self.assertTrue(np.isclose(np.std(dist.data),1, atol=0.1))

    def test_lognormal_distro(self):
        """"
        tests lognormal using Numpy methods
        """
        dist = NumpyDistributions('lognormal', mean=1, std=5, size=1000)
        self.assertEqual(dist.distribution, 'lognormal')
        self.assertEqual(len(dist.data), 1000)

    def test_laplace_distro(self):
        """"
        tests laplace using numpy methods
        """
        dist = NumpyDistributions('laplace', mean=2, std=1, size=1000)
        self.assertEqual(dist.distribution, 'laplace')
        self.assertEqual(len(dist.data), 1000)

    def test_invalid_distro(self):
        """"
        tests handling of invalid distribution type
        """
        with self.assertRaises(ValueError):
            NumpyDistributions('invalid', mean=0, std=1, size=1000)

    def test_negative_scale(self):
        """"
        tests invalid negative scale
        """
        with self.assertRaises(ValueError):
            dist = NumpyDistributions(dist='normal', mean=0, std=-1, size=1000)


if __name__ == '__main__':
    unittest.main()