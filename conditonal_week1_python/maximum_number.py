a=int(input("Enter A: "))
b=int(input("Enter B: "))
c=int(input("Enter C: "))

if a>b and a>c:
    maximum=a
elif b>c:
    maximum=b
else:
    maximum=c

print("Maximun NUmber is :",maximum)

