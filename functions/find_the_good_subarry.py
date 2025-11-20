def solve(self , A, B):
    N = len(A)
    count =0
    for i in range(N):
        sum =0
        for j in range(i,N):
            sum = sum+A[j] 
            if sum <B and (j-i+1)%2==0:
                count+=1
            if sum >B and (j-i+1)%2!=0:
                count+1
    return count


