n = int(input())
a = list(map(int,input().split()))

for i in range(len(a)):
    if(a[i]<0):
        print(a[i])