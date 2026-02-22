import os
import unittest

import autompg
from autompg import AutoMpg, AutoMPGData


class TestAutoMPG(unittest.TestCase):
    """
    Returns:
        Tests methods for autompg.py
    """
  #METHODS

    @classmethod
    def setUpClass(cls):
        """
        Returns:
            instantiates an object of the AutoMPGData class
        """
        cls.auto_tests = autompg.AutoMPGData()

    def setUp(self):
        """
        Returns:
            (String): Prints setUp
        """
        print("(⇀‸↼‶)⊃━☆ﾟ.*･｡ﾟ setUp")

    def test_str(self):
        """
        Returns:
            (String): Checks if the string being returned by the str
            method corresponds to the format AutoMPG('make', 'model', 'year', 'mpg')
        """
        print('Executing test_str ⊂(▀¯▀⊂ )')
        auto1 = self.auto_tests.data[0]
        expected_output = "AutoMPG('chevrolet', 'chevelle malibu', 1970, 18.0)"
        self.assertEqual(str(auto1),expected_output)

    def test_eq(self):
        """
        Returns:
            checks that the __eq__ method works using all four atts.
        """
        print('(つ▀¯▀ )つ Executing test_eq')
        auto3 = self.auto_tests.data[3]
        auto4 = self.auto_tests.data[4]

        self.assertNotEqual(auto3, auto4)
        self.assertEqual(auto3, auto3)


    def test_lt(self):
        """
        Returns:
            checks that the __lt__ method is working using all 4 atts.
        """
        print('Executing test_lt ⊂(▀¯▀⊂ )')

        auto4 = self.auto_tests.data[5]
        auto5 = self.auto_tests.data[6]

        self.assertTrue(auto5 < auto4)
        self.assertFalse(auto4 < auto5)


    def test_hash(self):
        """
        Returns:
            checks that the hash function is working properly
        """
        print('(つ▀¯▀ )つ Executing test_hash')
        auto6 = self.auto_tests.data[6]
        self.assertEqual(hash(auto6), hash(auto6))

    def tearDown(self):
        """
        Returns:
            (String): Prints tearDown
        """
        print("tearDown")


    @classmethod
    def tearDownClass(cls):
        """
        Returns:
            Deletes the auto-mpg.clean file
        """
        if os.path.exists('auto-mpg.clean'):
            os.remove('auto-mpg.clean')

        else:
            print('auto-mpg.clean not found')

if __name__ == '__main__':
    unittest.main()