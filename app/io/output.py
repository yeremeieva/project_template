
def write_console(output):
    """
     Function to write text from console

     :param output: Output to print.
     :return: The printed output.
     """
    print(output)


def write_python(file_path, text):
    """
    Function to write text to file

    :param file_path: Absolute path of the file
    :param text: Text to write
    :return: Written file.
    """
    try:
        with open(file_path, 'w') as file:
            file.writelines(text)
    except Exception as e_read:
        print(f'not successful read of txt, exception "{e_read}"')
