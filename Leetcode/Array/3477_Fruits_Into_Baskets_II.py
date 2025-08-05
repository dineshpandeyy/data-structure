class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        mySet = set()
        res = 0

        for fruit in fruits:
            for i in range(len(baskets)):
                if fruit <= baskets[i] and i not in mySet:
                    res += 1
                    mySet.add(i)
                    break
        
        return len(fruits) - res


        