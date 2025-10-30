numbers = []
for number in range(1, 101):
    numbers.append(number)

for number in numbers:
    if (number % 2 != 0) and (number % 3 == 0):
        numbers.remove(number)
    
print(len(numbers))