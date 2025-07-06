class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        maps = Counter(arr)
        result = 0

        for key, value in maps.items():
            if key == value:
                result = max(result, key)
        
        if result:
            return result
        
        return -1
        