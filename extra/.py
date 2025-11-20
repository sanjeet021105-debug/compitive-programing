# given an i check if ithe bit is set or not (set=1)

# n= int(input())

# i=int(input())
# if((n>>i)&1):
#     print("Set")
# else:
#     print("Unset")

# given an  integer n count how many set bit in n.

n= int(input())
i = int(input())
count=0

while(n>0):
    if n&1==1:
        count+=1
print(count)