def max
    N = len(C)
    maxV = 0
    for i in range(N):
        sum1= 0
        for j in range(i,N):
            sum1+=c[j]