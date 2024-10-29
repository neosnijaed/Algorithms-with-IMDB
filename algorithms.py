import csv

MOVIES_FILE = 'movies.csv'
IMDB_RATINGS_FILE = 'imdb_ratings.csv'
COMMA = ','
SEMICOLON = ';'


def create_csv_file(file_name) -> None:
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write('movie_title;imdb_rating\n')


def read_data_from_file(file_name) -> list:
    with open(file_name, 'r', encoding='utf-8') as r_file:
        reader = csv.reader(r_file, delimiter=COMMA)
        yield from reader


def write_data_to_file(data, file_name) -> None:
    with open(file_name, 'a', encoding='utf-8') as w_file:
        column_names = ['movie_title', 'imdb_rating']
        file_writer = csv.DictWriter(w_file, delimiter=SEMICOLON, lineterminator='\n', fieldnames=column_names)
        file_writer.writerow({'movie_title': data[0], 'imdb_rating': data[1]})


def read_data_from_dict(file_name) -> csv:
    with open(file_name, 'r', encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=SEMICOLON)
        yield from file_reader


def swap(arr: list, i: int, j: int) -> None:
    arr[i], arr[j] = arr[j], arr[i]


def found_binary(arr: list, value):
    low = 0
    high = len(arr)
    while low <= high:
        middle = int((low + high) / 2)
        if float(arr[middle][1]) == value:
            return middle
        elif float(arr[middle][1]) < value:
            low = middle + 1
        else:
            high = middle - 1
    return -1


def main() -> None:
    create_csv_file(IMDB_RATINGS_FILE)
    for line in read_data_from_file(MOVIES_FILE):
        write_data_to_file(line, IMDB_RATINGS_FILE)
    arr = list(read_data_from_dict(IMDB_RATINGS_FILE))
    arr.sort(key=lambda x: x[1])
    index = 0
    while index != -1:
        index = found_binary(arr, 6.0)
        if index != -1:
            print(f'{arr[index][0]} - {arr[index][1]}')
            del arr[index]


if __name__ == "__main__":
    main()
