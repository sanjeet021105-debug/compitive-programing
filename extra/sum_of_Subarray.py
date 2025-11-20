# print sum of every sub array
A = [1, 2, 3]

def sub_sum(A, S, E):
    total = 0
    for i in range(S, E + 1):
        total += A[i]
    print( total)

def Allsub_sum(A):
    N = len(A)
    for i in range(N):
        for j in range(i, N):
            sub_sum(A, i, j)

Allsub_sum(A)
