a = list(map(int,input().split()))
square=[]
for i in range(len(a)):
    square.append( a[i]*a[i])

print(square)