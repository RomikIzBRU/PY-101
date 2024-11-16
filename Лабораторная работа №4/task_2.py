import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
indent = 4
ensure_ascii = True

def task() -> None:
    with open(INPUT_FILENAME, encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=",", lineterminator="\n")
        lines = [line for line in reader]

    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as file:
        json.dump(lines, file, indent=indent, ensure_ascii=ensure_ascii)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
