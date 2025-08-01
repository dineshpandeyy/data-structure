class Solution:
    def numSplits(self, s: str) -> int:
        maps = Counter(s)
        visited = set()
        result = 0

        for char in s:
            visited.add(char)
            maps[char] -= 1

            if  maps[char] == 0:
                del  maps[char]

            if len(maps) == len(visited):
                result += 1
            
        return result



        