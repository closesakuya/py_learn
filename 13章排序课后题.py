#不使用排序，实现将一个字符串的大写、小写、数字分开存放，内部可无序

s = "AasadDasa121AadasSokl98901Aasad"

#若C为小写字母,返回0,大写返回2，数字返回1
def getord( c ):
    n = ord(c)
    if n >= 97 and n <= 122:
        return 0
    elif n >= 65 and n <= 90:
        return 2
    else:
        return 1


#桶排序实现方法
"""
rs = ['']*3

for item in s:
    rs[getord(item)]+= item
rt = ''
for item in rs:
    rt += item

print(rt)
"""

###使用国旗边界，快排思路

def quicksort(A):
    r = len(A)-1
    l = 0

    for i in range(len(A))[::-1]:  #右侧大写字符处理
        if getord(A[i]) == 2:
            temp = A[i]
            A[i] = A[r]
            A[r] = temp
            r -= 1

    for i in range(r):
        if getord(A[i]) == 0:   #左侧小写字符处理
            temp = A[i]
            A[i] = A[l]
            A[l] = temp
            l += 1        

ls = list(s)
quicksort(ls)
print(ls)
    
