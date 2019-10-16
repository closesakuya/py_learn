

#A为有序有重复数组
#查找第一个值等于K的元素下标
def B_Search_1( A, k):
    low = 0
    high = len(A) - 1

   
    isfind = False
    while( low <= high):
        mid = low + (high - low)//2
        if A[mid] == k:
            isfind = True
            break
        elif A[mid] >= k:
            high = mid - 1
        else:
            low = mid + 1

    if not isfind:
        return -1

    high = mid

    while(A[low]!= k):
        mid = low + (high - low)//2
        if mid == low:
            break
        if A[mid] == k:
            high = mid
        else:
            low = mid

    return high

#A为有序有重复数组
#查找最后一个值等于K的元素下标
def B_Search_2( A, k):
    low = 0
    high = len(A) - 1

   
    isfind = False
    while( low <= high):
        mid = low + (high - low)//2
        if A[mid] == k:
            isfind = True
            break
        elif A[mid] >= k:
            high = mid - 1
        else:
            low = mid + 1

    if not isfind:
        return -1

    low = mid

    while(A[high]!= k): #查询右边界
        mid = low + (high - low)//2
        if mid == low:
            break
        if A[mid] == k:
            low = mid
        else:
            high = mid

    return low


#A为有序有重复数组
#查找第一个值大于等于k的值
def B_Search_3( A, k):
    low = 0
    high = len(A) - 1

   
    isfind = False
    while( low <= high):
        mid = low + (high - low)//2
        if A[mid] == k:
            isfind = True
            break
        elif A[mid] >= k:
            high = mid - 1
        else:
            low = mid + 1

    if not isfind:
        return high+1  #查不到，返回大于改值第一个

    high = mid

    while(A[low]!= k):
        mid = low + (high - low)//2
        if mid == low:
            break
        if A[mid] == k:
            high = mid
        else:
            low = mid

    return high

#A为有序有重复数组
#查找最后一个值小于等于k的值
def B_Search_4( A, k):
    low = 0
    high = len(A) - 1

   
    isfind = False
    while( low <= high):
        mid = low + (high - low)//2
        if A[mid] == k:
            isfind = True
            break
        elif A[mid] >= k:
            high = mid - 1
        else:
            low = mid + 1

    if not isfind:
        return low-1  #查不到，返回小于改值最后

    low = mid

    while(A[high]!= k): #查询右边界
        mid = low + (high - low)//2
        if mid == low:
            break
        if A[mid] == k:
            low = mid
        else:
            high = mid

    return low


A = [1,1,2,2,2,2,3,5,5,7,7,7,7]

print(B_Search_4(A,6))
        
