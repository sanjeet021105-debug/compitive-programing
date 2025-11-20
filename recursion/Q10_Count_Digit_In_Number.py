def countDigit(n):
    if n<10:
        return 1
    return 1+countDigit(n//10)

n= int(input())
print(countDigit(n))
        
        