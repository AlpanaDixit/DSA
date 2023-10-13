def get(A ,index):
    if (index>=0 and index<len(A)):
        return A[index]
    
print(get([1,2,3,4,5], 4))


def set(A, index, x):
    if (index>=0 and index<len(A)):
        A[index] = x
        return A
    
print(set([1,2,3,4,5,6], 4, 10))

def avg(A):
    Total = 0
    n = len(A)
    for i in A:
        Total += i
    return Total/n

print(avg([1,2,3,4,5]))

def max(A):
    max = A[0]
    for i in range(1,len(A)):
        if max < A[i]:
            max = A[i]
    return max

print(max([1,2,3,4,5]))

def min(A):
    min = A[0]
    for i in range(1, len(A)):
        if min > A[i]:
            min = A[i]
    return min

print(min([1,2,3,4,5]))

def sum(A):
    total = 0
    for i in A:
        total += i
    return total

print(sum([1,2,3,4,5]))