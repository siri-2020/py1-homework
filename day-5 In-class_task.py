number = float(input())
output = ""

if number % 2 == 0:
    output = "A"
    if number % 3 == 0:
        output = "C"
    else:
        output = "B"
else:
    output = "D"
print(output)