a = list(map(int,input().split()))
b = list(map(int,input().split()))

result =[]

for i in range(len(a)):
    result+= [(a[i]+b[i])]
print(result)