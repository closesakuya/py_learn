class cyclequeue():
    def __init__(self, size):
        self._arr = [None]*size
        self._size = size
        self._head = 0
        self._tail = 0

    def dequeue(self):
        if self._head == self._tail:
            print("is None")
            return None
        self._head = (self._head+1)%self._size
        print("Queue is{0}".format(self._arr))
        return self._arr[(self._head-1)%self._size]

    def enqueue(self,obj):
        if self._head == (self._tail+1)%self._size:
            print("is Full")
            return False
        self._arr[self._tail] = obj
        self._tail = (self._tail+1)%self._size
        print("Queue is{0}".format(self._arr))
        return True

        
    
