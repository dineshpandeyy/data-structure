class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sortedArr = sorted(score)[::-1]
        maps = {}
        for i, value in enumerate(sortedArr):
            maps[value] = i
        print(maps)

        result = []
        for i, value in enumerate(score):
            index = maps[value]
            if index == 0:
                result.append("Gold Medal")
            elif index == 1:
                result.append("Silver Medal")
            elif index == 2:
                result.append("Bronze Medal")
            else:
                result.append(str(index+1))
        
        return result

        