# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    data = []
    with open(INPUT_FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

            # Сериализация данных в JSON формат
        with open(OUTPUT_FILENAME, 'w') as file:
            json.dump(data, file, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
