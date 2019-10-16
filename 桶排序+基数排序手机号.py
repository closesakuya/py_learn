dataset = [
    "13788594523",
    "3836887",
    "14463434676",
    "13123523623"
    ]

def bucket_sort(A,idx):
    dct = {}
    for i in range(10):
        dct[i]=[]

    for item in A:
        try:
            val = int(item[idx])
        except IndexError:
            val = 0

        dct[val].append(item)

    lst = []
    for item in dct.values():
        lst += item
    print(idx,lst)
    return lst



##只操作下标
def bucket_sort_s(A, idxlst, key):
    dct = [[]]*10
    for item in idxlst:
        try:
            val = int(A[item][key])
        except KeyError:
            val = 0
        dct[val].append(item)
    ret = []
    for item in dct:
        ret += item
    return ret



maxlen = 11

#通过11个号码位的排序
#排序11次
for i in range(maxlen)[::-1]:
    dataset = bucket_sort(dataset, i)

print(dataset)


    
            
