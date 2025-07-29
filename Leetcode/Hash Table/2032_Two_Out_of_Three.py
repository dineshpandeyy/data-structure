class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        mySet = defaultdict(int)

        for num in set(nums1):
            mySet[num] += 1
        
        for num in set(nums2):
            mySet[num] += 1
        
        for num in set(nums3):
            mySet[num] += 1
        
        res = []
        for key, value in mySet.items():
            if value >= 2:
                res.append(key)
        return res


            

        