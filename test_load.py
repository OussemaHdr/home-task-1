import unittest
from etl.etl import get_from_csv

class TestETLPipeline(unittest.TestCase):
    def test_extract_data(self):
        csv_file_path = "data/sample.csv"
        data = get_from_csv(csv_file_path)

        # Assert data is not empty and is of the expected type
        self.assertTrue(data)
        self.assertIsInstance(data, list)

if __name__ == '__main__':
    unittest.main()