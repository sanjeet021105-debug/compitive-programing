a = list(map(int,input().split()))
n = len(a)
rev =[]

for i in range(n-1,-1,-1):
    rev.append(a[i])
print(rev)