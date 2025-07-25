from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.maxValue = 0
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        
    def push(self, val: int) -> None:
        value =  self.freq[val] + 1
        self.maxValue = max(self.maxValue, value)
        self.freq[val] = value

        self.group[value].append(val)

    def pop(self) -> int:
        val = self.group[self.maxValue].pop()
        self.freq[val] -= 1

        if not self.group[self.maxValue]:
            self.maxValue -= 1
        
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()