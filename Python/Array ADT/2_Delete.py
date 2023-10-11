def Delete(A,index):
    x = A[index]
    length = (len(A)-1)
    for i in range(index,length-1):
        A[i]=A[i+1]
    length -= 1
    print(A)

list=[1,2,3,4,5,6]
Delete(list,3)

list1=[1,2,3,4,5,6]
del list1[3]
print(list1)
# def delete(A, index):

#     x = 0
#     if (index>0 and index<len(A)):
#         x=A[index]