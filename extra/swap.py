list = [10,20,30,40,50]

print(list)

for i in range(len(list)//2):
    list[i], list[-i-1]=list[-i-1], list[i]
print(list)


print(list.reverse)
