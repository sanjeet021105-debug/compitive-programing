num = int(input("Enter a number: "))
largest = 0
temp = num

while temp > 0:
    digit = temp % 10
    if digit > largest:
        largest = digit
    temp = temp // 10

if largest == 4:
    print(" largest digit is 4.")
else:
    print(" largest digit is not 4.")
