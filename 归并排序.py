
#merge_sort(p…r) = merge(merge_sort(p..q),merge_sort(q,r))


def merge(lst1, lst2):
    lst = []
    i = 0
    j = 0
    lst1 += [float('inf')] ##哨兵元素，防止遍历越界
    lst2 += [float('inf')]
    #print(lst1, lst2)
    while( i < len(lst1) and j < len(lst2) ):
        if lst1[i] <= lst2[j]:
            lst.append(lst1[i])
            i += 1
        else:
            lst.append(lst2[j])
            j += 1
    return lst[:-1]
        
        
    


def merge_sort( lst ):
    if len(lst ) <= 1:
        return lst
    return merge(merge_sort(lst[:int(len(lst)/2)]), merge_sort(lst[int(len(lst)/2):]))






###使用原数组 操作下标
def merge0(A):
    return merge_sortS(A,0,len(A) - 1)

def mergeS(A, p,q,r):
    lst = []
    i = p
    j = q+1
    while( i <= q and j <= r):
        if A[i] <= A[j]:
            lst.append(A[i])
            i += 1
        else:
            lst.append(A[j])
            j += 1

    lst += A[i:q+1]
    lst += A[j:r+1]
    for i in range(len(lst)):
        A[p + i] = lst[i]

def merge_sortS(A, p, r):
    if p >= r:
        return
    mid = int((r + p)/2)
    merge_sortS(A, p ,mid)
    merge_sortS(A, mid+1, r)
    mergeS(A,p,mid,r)



a = [1,3,656,1,3,8979,4,2,54535,232,777777,1,2,3,2,4,666,323]
#a = merge_sort(a)
merge0(a)
print(a)
