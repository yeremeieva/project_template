import os
import pandas as pd


def read_console(prompt=""):
    """
     Function to read text from console with prompt

     :param prompt: Optional text before the input
     :return: The input from user.
     """
    return input(prompt)
    pass


def read_python(file_path):
    """
    Function to read text from file

    :param file_path: Absolute path of the file
    :return: Text from file.
    """
    if not os.path.exists(file_path):
        print(f'{file_path} does not exist (hint: try absolute path)')
        return
    try:
        with open(file_path, "r") as file:
            return file.read()
    except Exception as e_read:
        print(f'not successful read of file, exception "{e_read}"')


def read_pandas(file_path):
    """
    Function to read data from a CSV file using the pandas library.

    :param file_path: Path to the CSV file.
    :return: DataFrame with the data.
    """
    if not os.path.exists(file_path):
        print(f'{file_path} does not exist (hint: try absolute path)')
        return
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f'not successful read of csv, exception: {e}')
        return None

