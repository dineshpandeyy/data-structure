from collections import defaultdict
class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:

        conflictingMaps = defaultdict(list)
        for a, b in conflictingPairs:
            low = min(a, b)
            high = max(a, b)
            conflictingMaps[high].append(low)
        
        largest = 0
        secondLargest = 0
        extraArr = [0] * (n+1)
        valid = 0
        for i in range(1, n + 1):
            for u in conflictingMaps[i]:
                if u >= largest:
                    secondLargest = largest
                    largest = u
                elif u > secondLargest:
                    secondLargest = u
            
            valid += i - largest

            extraArr[largest] += largest - secondLargest

        
        return max(extraArr) + valid

                




            