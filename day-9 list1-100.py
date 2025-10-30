numbers = list(range(1, 101))

final_list = []
for index in numbers:
    if not (index % 2 == 1 and index % 3 == 0):
        final_list.append(index)
print(final_list)
print("How many number left:", len(final_list))