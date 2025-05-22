import sys


def read_numbers(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return [int(line.strip()) for line in lines]


def calculate_min_number_of_moves(numbers, min_number):
    return sum(abs(number - min_number) for number in numbers)


def main(numbers_path):
    numbers = read_numbers(numbers_path)
    avg = round(sum(numbers) / len(numbers))
    min_number = min(numbers, key=lambda x: abs(x - avg))
    number_of_moves = calculate_min_number_of_moves(numbers, min_number)
    print(number_of_moves)

main(sys.argv[1])
