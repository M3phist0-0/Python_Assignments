import unittest
import shelter
from shelter import Shelter, Tent, Tarp, Hammock

class TestShelter(unittest.TestCase):
    """
    Returns:
        Tests each method for shelter.py
    """

    @classmethod
    def setUpClass(cls):
        """
        Returns:
            (String): Prints setUpClass
        """
        print('(⇀‸↼‶)⊃━☆ﾟ.*･｡ﾟ setUpClass')

    def setUp(self):
        """
        Returns:
            (String): prints executing setUp created shelter objects for testing
        """
        print('Executing setUp...')
        self.tent1 = shelter.Tent(num_occupants=2, material='polyester', setup_time=3, weight=10.5, seasons=4, sqft=20.0, vestibule=True, structure_poles=True)
        self.tent2 = shelter.Tent(num_occupants=3, material='polyester', setup_time=5, weight=12.5, seasons=3, sqft=28.0, vestibule=False, structure_poles=True)
        self.tarp1 = shelter.Tarp(num_occupants=2, material='canvas', setup_time=3, weight=10.5, seasons=4, sqft=20.0)
        self.tarp2 = shelter.Tarp(num_occupants=3, material='canvas', setup_time=5, weight=12.5, seasons=3, sqft=28.0)
        self.hammock1 = shelter.Hammock(num_occupants=2, material='cotton', setup_time=3, weight=10.5, seasons=4, length=11)
        self.hammock2 = shelter.Hammock(num_occupants=3, material='cotton', setup_time=5, weight=12.5, seasons=3, length=14)



    def test_str(self):
        """
        Returns:
            (String): Prints executing tes_str checks if format for the str
            method prints properly
        """
        print('Executing test_str...⊂(▀¯▀⊂ )')
        tent_expected = "Shelter(2, 'polyester', 3, 10.5, 4, 20.0, True, True)"
        self.assertEqual(str(self.tent1), tent_expected)

        tarp_expected = "Shelter(2, 'canvas', 3, 10.5, 4, 20.0)"
        self.assertEqual(str(self.tarp1), tarp_expected)

        hammock_expected = "Shelter(2, 'cotton', 3, 10.5, 4, 11)"
        self.assertEqual(str(self.hammock1), hammock_expected)


    def test_lt(self):
        """
        Returns:
            (String): Prints executing test_lt checks that the __lt__
            method is working properly
        """
        print('Executing test_lt...⊂(▀¯▀⊂ )')

        #tent testing
        self.assertFalse(self.tent1 == self.tent2)
        self.assertTrue(self.tent1 < self.tent2)
        self.assertFalse(self.tent2 < self.tent1)

        #tarp testing
        self.assertFalse(self.tarp1 == self.tarp2)
        self.assertTrue(self.tarp1 < self.tarp2)
        self.assertFalse(self.tarp2 < self.tarp1)

        #hammock testing
        self.assertFalse(self.hammock1 == self.hammock2)
        self.assertTrue(self.hammock1 < self.hammock2)
        self.assertFalse(self.hammock2 < self.hammock1)




    def test_is_better(self):
        """
        Returns:
            (String): Prints is_better checks if the if_better method is working
            properly
        """
        print('Executing is_better...⊂(▀¯▀⊂ )')

        #tent test
        self.assertTrue(self.tent1.is_better(self.tent2))
        self.assertFalse(self.tent2.is_better(self.tent2))

        #tarp test
        self.assertTrue(self.tarp1.is_better(self.tarp2))
        self.assertFalse(self.tarp2.is_better(self.tarp1))

        #hammock test
        self.assertTrue(self.hammock1.is_better(self.hammock2))
        self.assertFalse(self.hammock2.is_better(self.hammock1))



    def tearDown(self):
        """
        Returns:
            string: print executing tearDown deletes objects created in
            setUp
        """
        print('(つ▀¯▀ )つ Executing tearDown...')
        del self.tent1
        del self.tent2
        del self.tarp1
        del self.tarp2
        del self.hammock1
        del self.hammock2


    @classmethod
    def tearDownClass(cls):
        """
        Returns:
            (String): Prints tearDownClass
        """
        print('tearDownClassヽ(⌐■_■)ノ♪♬')

if __name__ == '__main__':
    unittest.main()