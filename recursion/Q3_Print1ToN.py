def PrintNumber1toN(n):
    if n==0:
        return 
    PrintNumber1toN(n-1)
    print(n)

n= int(input())

PrintNumber1toN(n)