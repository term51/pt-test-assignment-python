import sys


def main(numbers_path):
    numbers = []
    with open(numbers_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        numbers.append(int(line.strip()))

    avg = round(sum(numbers) / len(numbers))

    min_number = numbers[0]
    for number in numbers:
        min_number = number if abs(number - avg) < abs(min_number - avg) else min_number

    count = 0
    for number in numbers:
        count += abs(number - min_number)
    print(count)


main(sys.argv[1])
