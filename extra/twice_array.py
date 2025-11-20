# given N array elements every elements repeat twice except 1. find the unique element. 

arr= list(map(int,input().split()))
answer =0
for i in range(len(arr)):
    answer=answer^arr[i]
    
print(answer)