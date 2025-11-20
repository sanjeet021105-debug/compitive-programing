T = int(input())
s = [input() for _ in range(T)]
palindrom=0
not_palindrom=0
if s ==s[::-1]:
    palindrom+=1
else:
    not_palindrom+=1

print(palindrom)
print(not_palindrom)