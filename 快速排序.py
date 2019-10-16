#quick_sort(p..r) = quick_sort(p..q) + quick_sort(q+1,r)


#p..r下标均可遍历到,为闭区间，故r取n-1
def sort(A):
    return quick_sort(A,0,len(A)-1)
def quick_sort(A,p,r):
    if p >= r:
        return

    #获取分区点，分区点左边数全小于分区点，右边数全大于分区点
    mid = partition(A,p,r)

    quick_sort(A,p,mid-1)
    quick_sort(A,mid+1,r)



##时间复杂度高
##初次尝试
def partition_drop(A,p,r):
    #参考插入排序
    #选取末尾元素r为pivot
    #使用j倒叙遍历r-1.....p,取var = A[r-1]，若var<= pivot,不操作，
    #否则，将r-j...r元素全左移一位，var放入末尾
    pivot = A[r]
    for j in range(p,r)[::-1]:
        var = A[j]
        if var > pivot:
            for idx in range(j,r):
                A[idx] = A[idx+1]
            A[r] = var


#实际实现
def partition(A, p, r):
    """
    取pivot = A[r]
    通过游标div,左到右遍历A，保证  p..div-1为小于pivot区间 div..r-1为大于ivot区间
    """
    pivot = A[r]
    div = p
    for j in range(p,r+1):
        if A[j] <= pivot:
            temp = A[div]
            A[div] = A[j]
            A[j] = temp
            div += 1
    #print(div)
    #游标div始终指向最新未处理值
    #div值最终为小于pivot的值的数量+1
    #返回mid用作区间切割

    return (div-1)


A = [1,5,3,2,7,9,10,4,23,999,1,2,777,3,4]
sort(A)
print(A)
