# given an array and increment number genrate a new all array which cantians all value of orginial array increase by increment value .

arr = list(map(int,input().split()))
value = int(input())
new_arr = [x + value for x in arr ]
print(new_arr)


# given a list of interger and a target number find and print index of target number in the list .

# arr = list(map(int,input().split()))
# x = int(input())
# ...
# for i in range(len(arr)):
#     if x == arr[i]:
#         print(i)
        
    