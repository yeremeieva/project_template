from app.io.input import read_python, read_pandas

import unittest
import os
import pandas as pd


class TestReadFunctions(unittest.TestCase):
    def test_read_python_file_exists(self):
        file_path = "test_file.txt"
        with open(file_path, "w") as file:
            file.write("I love unit tests")

        result = read_python(file_path)
        self.assertEqual(result, "I love unit tests")
        os.remove(file_path)

    def test_read_python_file_not_exists(self):

        file_path = "no_file.txt"
        result = read_python(file_path)
        self.assertIsNone(result)

    def test_read_pandas_file_exists(self):

        file_path = "test_data.csv"
        test_data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        test_data.to_csv(file_path, index=False)

        result = read_pandas(file_path)

        self.assertTrue(isinstance(result, pd.DataFrame))
        self.assertEqual(len(result), 3)
        self.assertEqual(list(result.columns), ['A', 'B'])

        os.remove(file_path)

    def test_read_pandas_file_not_exists(self):

        file_path = "nonexistent_data.csv"
        result = read_pandas(file_path)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
