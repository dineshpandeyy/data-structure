class MyCircularDeque:

    def __init__(self, k: int):
        self.front = 0
        self.last = k - 1
        self.total = 0
        self.deque = [0] * k
        self.k = k
        
    def insertFront(self, value: int) -> bool:
        if self.total < self.k:
            self.front = (self.front - 1 + self.k) % self.k
            self.deque[self.front] = value
            self.total += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.total < self.k:
            self.last = (self.last + 1) % self.k
            self.deque[self.last] = value
            self.total += 1
            return True
        return False
        
    def deleteFront(self) -> bool:
        if self.total > 0:
            self.front = (self.front+1) % self.k
            self.total -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if self.total > 0:
            self.last = (self.last-1 + self.k) % self.k
            self.total -= 1
            return True
        return False
        
    def getFront(self) -> int:
        if self.total > 0:
            return self.deque[self.front]
        return -1
        

    def getRear(self) -> int:
        if self.total > 0:
            return self.deque[self.last]
        return -1
        
    def isEmpty(self) -> bool:
        return self.total == 0
        
    def isFull(self) -> bool:
        return self.total == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()