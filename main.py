from app.io.input import read_python, read_console, read_pandas
from app.io.output import write_python, write_console


def main():
    path = '.../files'
    my_name = read_console("Write your name ")

    write_console(f"{my_name} is a beautiful name")

    txt = read_python(f'{path}/short.txt')
    write_console(f'{my_name} reads about \n {txt}')
    write_python(f'{path}/local.txt', f"Let's remember that {my_name} reads about {txt}")

    csv = read_pandas(f'{path}/missile_attacks_daily.csv')
    write_console(csv.head())


if __name__ == '__main__':
    main()
