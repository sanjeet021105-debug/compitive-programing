a = list(map(int,input().split()))
count_even=0
count_odd=0
difference =0

for i in range(len(a)):
    if(a[i]%2==0):
        count_even+=1
    elif(a[i]%2!=0):
        count_odd+=1
    difference=abs(count_odd-count_even)
print(difference)