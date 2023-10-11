def linear_search(Arr, k):
    for i in range(0,(len(Arr))):
        if Arr[i] == k:
            return i
    return False

print(linear_search([1,2,3,4,5,6],6))

def linear_search_transposition(Arr, k):
    for i in range(0,(len(Arr))):
        if Arr[i] == k:
            Arr[i], Arr[i-1] = Arr[i-1], Arr[i] 
            return i -1
    return False

print(linear_search([1,2,3,4,5,6],6))

def linear_search_move_to_front(Arr, k):
    for i in range(0,(len(Arr))):
        if Arr[i] == k:
            Arr[0], Arr[i] = Arr[i], Arr[0] 
            return 0
    return False
