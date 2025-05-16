'''
767. Reorganize String

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 
Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.
'''
import heapq

def reorganize(string):
    maps = {}

    for char in string:
        if char not in maps:
            maps[char] = 1
        else:
            maps[char] += 1
            if maps[char] > (len(string) +1)// 2:
                return ""
        
    heap = [(-value, char) for char, value in maps.items()]

    heapq.heapify(heap)
    result = []
    while len(heap) >= 2:
        firstLargestVal, firstLargestElem = heapq.heappop(heap)
        secondLargestVal, secondLargestElem = heapq.heappop(heap)

        result.append(firstLargestElem)
        firstLargestVal += 1
        result.append(secondLargestElem)
        secondLargestVal += 1

        if firstLargestVal < 0:
            heapq.heappush(heap, (firstLargestVal, firstLargestElem))
        
        if secondLargestVal < 0:
            heapq.heappush(heap, (secondLargestVal, secondLargestElem))
    
    if heap:
        result.append(heap[0][1])
    
    return "".join(result)



s = "aab"
print(reorganize(s))

s = "aaab"
print(reorganize(s))


