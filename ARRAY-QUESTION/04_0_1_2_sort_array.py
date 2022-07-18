# GIVEN ARRAY CONSIST OF ONLY    ,   1 , 2  & 0 
# SORT THE ARRAY WITHOUT USING SORT ALGORITHM
# EXAMPLE---->  INPUT ----> 0,1,2,0,2,1   
#            OUTPUT ----> 0,0,    1,1,        2,2
#                         left   current     Right
#                          LO       Mid        HI
def SortArray( a, arr1):
    low = 0
    hi = arr1 - 1
    mid = 0
    while mid < hi:
        if a[mid] == 0:
            a[low], a[mid] = a[mid], a[low]
            low = low + 1
            mid = mid + 1
        elif a[mid] == 1:
            mid = mid + 1
        else:
            a[mid], a[hi] = a[hi], a[mid] 
            hi = hi - 1
    return a
    

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
arr1 = len(arr)
arr = SortArray( arr, arr1)
print(arr)
