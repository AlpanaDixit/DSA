

def BinarySearch(A ,l , h, key):
    while(l<=h):
        mid = (l+h)//2
        if key ==  A[mid]:
            return mid
        elif key < A[mid]:
            h = mid -1
        else:
            l = mid + 1
    return -1


A = [4, 8, 10, 15, 18, 21, 24, 27, 29, 33, 34, 37, 39, 41, 43]
l = 0
h = len(A) - 1
key = 18

print(BinarySearch(A ,l , h, key))


def RBinarySearch(A, l, h, key):
    if (l<=h):
        mid = (l+h)//2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            return RBinarySearch(A, l, mid-1, key)
        else:
            return RBinarySearch(A, mid+1, h, key)
    return -1

A = [4, 8, 10, 15, 18, 21, 24, 27, 29, 33, 34, 37, 39, 41, 43]
l = 0
h = len(A) - 1
key = 18

print(RBinarySearch(A ,l , h, key))