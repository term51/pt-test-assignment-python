n = int(input("Enter N - length of circular array: "))
m = int(input("Enter M - interval length: "))

circular_array = [i for i in range(1, n + 1)]
i = 0
part_of_path = []
full_path = []

while True:
    next_index = i % len(circular_array)
    part_of_path.append(circular_array[next_index])

    if len(part_of_path) == m:
        i -= 1
        full_path.append(part_of_path[0])

        if part_of_path[-1] == circular_array[0]:
            break

        part_of_path = []

    next_element = circular_array[next_index]
    i += 1

print("".join(str(x) for x in full_path))
