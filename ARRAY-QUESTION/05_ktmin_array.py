from numpy import sort


def Kthsmallest(arr,size,k):
    arr.sort()
    return arr[k-1]

arr=[11,2,34,4,6]
size=len(arr)
k=2
arr=Kthsmallest(arr,size,k)
print(arr)