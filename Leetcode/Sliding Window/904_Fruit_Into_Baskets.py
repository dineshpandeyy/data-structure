class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        maps = {}
        left = 0
        res = 0

        for right in range(len(fruits)):
            fruit = fruits[right]
            if fruit not in maps:
                maps[fruit] = 1
            else:
                maps[fruit] += 1
            
            while len(maps) > 2:
                maps[fruits[left]] -= 1
                if maps[fruits[left]] == 0:
                    del maps[fruits[left]]   
                left += 1
            
            res = max(res, right - left + 1)
        
        return res
        