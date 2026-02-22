import unittest
from collections import Counter
import assignment4
from assignment4 import Records, InvalidColumnNames, NoRecordStatsFound

class TestCollections(unittest.TestCase):
    """"
    Tests to validate the functionality of assignment4.py
    """
    @classmethod
    def setUpClass(cls):
        """"
        Prints set up class and instantiates an object from the Record class
        """
        print("setUpClass⊂(▀¯▀⊂ )")
        cls.credit_card = assignment4.Records('credit_card.csv', 'credit card')
        cls.customer_complaints = assignment4.Records('customer_complaints.csv', 'customer complaints')
        cls.credit_card.load_data()
        cls.customer_complaints.load_data()


    def setUp(self):
        """"
        Prints setUp
        """
        print("setUp")

    def tearDown(self):
        """"
        prints tearDown
        """
        print("tearDown")

    def test_create_container(self):
        """"
        Tests the test_create_container function.
        - validates the correct behavior for valid column names
        """
        print('Executing test_create_container')
        header = ['Period', 'Amount', 'Category', 'Word']
        container = self.credit_card._create_container(header)

        self.assertEqual(container._fields, ('period', 'amount', 'category', 'word'))


    def test_record_stats(self):
        """"
        Tests the record_stats function.
        - Verifies that stats are computed correctly for a valid column.
        - Ensures that NoRecordStatsFound exception is raised for a non-existent column.
        """
        print('Executing test_records_stats')

        column_name, stats = self.credit_card.record_stats('credit card', 'Period', lambda x: x)
        self.assertEqual(column_name, 'period')
        self.assertIsInstance(stats, Counter)

        with self.assertRaises(NoRecordStatsFound):
            self.credit_card.record_stats('credit card', 'InvalidColumn', lambda x: x)



    def test_extract_top_n(self):
        """"
        Tests the extract_top_n function
        - Verifies the correct retrieval of top n most common values.
        - Ensures that NoRecordStatsFound exception is raised if stats are not available.

        """

        print('Executing test_extract_top_n')

        self.credit_card.record_stats('credit card', 'Period', lambda x: x)


        top_n = self.credit_card.extract_top_n(5, 'credit card', 'Period')
        self.assertIsInstance(top_n, list)
        self.assertTrue(len(top_n) <= 5)


        with self.assertRaises(NoRecordStatsFound):
            self.credit_card.extract_top_n(5, 'credit card', 'InvalidColumn')

    @classmethod
    def tearDownClass(cls):
        """"
        Prints tearDownClass to console and deletes the instances of Record class
        """
        print("tearDownClass ᕕ(⌐■_■)ᕗ ♪♬")
        del cls.credit_card
        del cls.customer_complaints
        print('┬─┬ノ(ಠ_ಠノ) ')

if __name__ == '__main__':
    unittest.main()