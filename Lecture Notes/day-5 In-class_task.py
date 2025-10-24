number = int(input())

if number % 2 == 0:
    if number % 3 == 0:
        print("C")
    else:
        print("B")
else:
    print("D")