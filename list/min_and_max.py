N = int(input())
a = list(map(int,input().split()))

maximum = a[0]
minimum = a[0]

for i in a:
    if i>maximum:
        maximum = i
    elif i<minimum:
        minimum =i

print("maximun: ",maximum)            
print("minimum: ",minimum)            
    


