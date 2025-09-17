n = int(input())
a = list(map(int,input().split()))
maximum =[]
minimum =[]
for i in range(len(a)):
    maximum = max(a)
    minimum = min(a)
print(maximum)
print(minimum)
