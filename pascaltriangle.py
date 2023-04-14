# pascaltriangle
rows = int(input("Enter the number of rows: "))

for i in range(rows):
    for space in range(1, rows-i+1):
        print("  ", end="")
    for j in range(i+1):
        if j == 0 or i == 0:
            c = 1
        else:
            c = c * (i-j+1) // j
        print("{:4d}".format(c), end="")
    print()
