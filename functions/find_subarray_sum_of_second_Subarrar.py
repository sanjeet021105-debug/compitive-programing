a = int(input())
b = int(input())
N= len(a)
count =0
for i in range(N):
    
    sum =0
    for j in range(i,N):
        sum = sum +a[j]
        if sum <b:
            count+=1
print(sum)
# return count

