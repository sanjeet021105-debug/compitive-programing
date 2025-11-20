def PrintNumberNto1(n):
    if n==0:
        return 
    print(n)
    PrintNumberNto1(n-1)

n= int(input())

PrintNumberNto1(n)