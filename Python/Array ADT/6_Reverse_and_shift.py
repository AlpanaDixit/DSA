def reverse(A):
    left = 0
    right = len(A)-1
    while left<=right:
        temp = A[left]
        A[left] = A[right]
        A[right] = temp
        left += 1
        right -= 1
    return A

print(reverse([1,2,3,4,5,6]))