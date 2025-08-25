n = int(input("Enter N: "))
for i in range(1, n+1):
    for j in range(n-i):
        print("_", end="")

    for k in range(i):
        print("*", end="")

    print()
