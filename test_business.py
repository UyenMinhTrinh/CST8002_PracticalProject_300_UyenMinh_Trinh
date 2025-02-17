import unittest
from business import Business
from record import Record

class TestBusinessLogic(unittest.TestCase):
    def setUp(self):
        self.records = [
            Record("12345", "TestCity", 2000, "Dwelling Units", 400.0),
            Record("12346", "SampleTown", 2010, "Dwelling Units", 450.0)
        ]
        self.business = Business(self.records)

    def test_find_record(self):
        result = self.business.find_record(2000)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].csd, "TestCity")

    def test_add_record(self):
        new_record = Record("12347", "NewCity", 2022, "Dwelling Units", 500.0)
        self.business.add_record(new_record)
        self.assertEqual(len(self.business.records), 3)

    def test_update_record(self):
        updated = self.business.update_record(2000, 420.0)
        self.assertTrue(updated)
        self.assertEqual(self.business.find_record(2000)[0].value, 420.0)

    def test_delete_record(self):
        self.business.delete_record(2000)
        self.assertEqual(len(self.business.records), 1)
        self.assertEqual(self.business.records[0].csd, "SampleTown")

if __name__ == "__main__":
    unittest.main()
