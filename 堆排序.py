import copy
class Node( ):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __lt__(self, other):
        return True if self.value < other.value else False
    def __le__(self, other):
        return True if self.value <= other.value else False
    def __gt__(self, other):
        return True if self.value > other.value else False
    def __ge__(self, other):
        return True if self.value >= other.value else False

class Heap():
    def __init__(self,arr = None,capacity = 10):
        self.capacity = capacity
        if arr:
            self.capacity = len(arr)
            self._arr = [None]+arr[::]
            self.num = len(arr)
            self.buildheap()
        else:
            self._arr = [None]*self.capacity
            self.num = 0

    def __str__(self):
        return str(list(map(str,self._arr))[1:])

    def insert(self,node):

        if self.num >= self.capacity:
            return False

        self.num += 1
        pos = self.num

        self._arr[self.num] = node
        #插入尾部
        while pos > 1 and self._arr[pos//2] < self._arr[pos]:
            temp = self._arr[pos//2]
            self._arr[pos//2] = self._arr[pos]
            self._arr[pos] = temp
            pos = pos//2
        return True

    def buildheap(self):
        #对输入的任意self._arr进行堆化
        for i in range(1,self.num//2 + 1)[::-1]:
            self.heapify(self.num,i)


    def heapify(self,n,i):
        #堆化，以i为子堆顶，n为最后一个叶子下标
        pos = i        
        while pos <= n:
            maxpos = pos
            if pos*2 <= n and self._arr[maxpos] < self._arr[pos*2]:
                maxpos = pos*2
            if ((pos*2) + 1) <= n and self._arr[maxpos] < self._arr[(pos*2) + 1]:
                maxpos = (pos*2) + 1
            temp = self._arr[pos]
            self._arr[pos] = self._arr[maxpos]
            self._arr[maxpos] = temp

            if maxpos == pos:
                break
            pos = maxpos

            
        



    def removetop(self):
        if not self._arr[1]:
            return None

        ret = self._arr[1]
        self._arr[1] = self._arr[self.num]
        self._arr[self.num] = None
        self.num -= 1
        pos = 1

        while pos <= self.num:
            maxpos = pos
            if pos*2 <= self.num and self._arr[maxpos] < self._arr[pos*2]:
                maxpos = pos*2
            if ((pos*2) + 1) <= self.num and self._arr[maxpos] < self._arr[(pos*2) + 1]:
                maxpos = (pos*2) + 1
            temp = self._arr[pos]
            self._arr[pos] = self._arr[maxpos]
            self._arr[maxpos] = temp

            if maxpos == pos:
                break
            pos = maxpos
        return ret

    def sortoutput(self):
        ret = []
        bak = self._arr[::]
        baknum = self.num
        while True:
            out = self.removetop()
            if out:
                ret.append(out)
            else:
                break
        self.num = baknum
        self._arr = bak[::]

        return ret[::]

        

"""
aa = Heap(15)
aa.insert(Node(10))
aa.insert(Node(11))
aa.insert(Node(22))
aa.insert(Node(55))
aa.insert(Node(33))
aa.insert(Node(12))
aa.insert(Node(44))
aa.insert(Node(13))
aa.insert(Node(17))
print(aa)

aa.removetop()
print(aa)
"""
a = Heap([11,12,23,45,1,35,76,88])
print(a)

b = a.sortoutput()
print(b)
