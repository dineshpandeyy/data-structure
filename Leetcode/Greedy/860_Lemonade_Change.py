class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiveCount = 0
        tenCount = 0
        twentyCount = 0


        for bill in bills:
            if bill == 5:
                fiveCount += 1
            elif bill == 10:
                if fiveCount:
                    fiveCount -= 1
                    tenCount += 1
                else:
                    return False
            else:
                if tenCount and fiveCount:
                    tenCount -= 1
                    fiveCount -= 1
                elif fiveCount >= 3:
                    fiveCount -= 3
                else:
                    return False
        
        return True