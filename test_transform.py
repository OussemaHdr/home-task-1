import unittest
from etl.etl import transform

class TestETLPipeline(unittest.TestCase):
    def test_transform_data(self):
        sample_data = [
            {"fullname": "John Doe", "age": 25, "location": "New York"},
            {"fullname": "Jane Smith", "age": 30, "location": "Los Angeles"}
        ]

        transformed_data = transform(sample_data)

        # Assert transformed_data is not empty and is of the expected type
        self.assertTrue(transformed_data)
        self.assertIsInstance(transformed_data, list)

if __name__ == '__main__':
    unittest.main()