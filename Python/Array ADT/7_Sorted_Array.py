def isSorted(A, n):
    print(n)
    print(range(0,n-1))
    for i in range(0,n):
        print(i)
        print(A[i], A[i+1])
        if(A[i]>A[i+1]):
            return False
    return True

A = [4,8,13,26,20,25,28,33]
n = len(A)-1
print(isSorted(A,n))
