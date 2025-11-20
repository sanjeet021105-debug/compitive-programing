# print all subarray of given 
A=[1,2,3]
def sub (A,S,E):
    for i in range(S,E+1):
        print(A[i],end=" ")
    print()
def Allsub (A):
    N = len(A)
    for i in range(N):
        for j in range(i,N):
            sub(A,i,j)
Allsub(A)


