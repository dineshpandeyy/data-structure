class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.nums1 = nums1
        self.nums2 = nums2
        self.maps = Counter(nums2)
        

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        oldValue = self.nums2[index]
        newValue = oldValue + val
        self.maps[oldValue] -= 1
        if self.maps[oldValue] == 0:
            del self.maps[oldValue]

        self.maps[newValue] += 1
        self.nums2[index] = newValue


    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        res = 0
        for num in self.nums1:
            val = tot - num
            if val in self.maps:
                res += self.maps[val]
        
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)