class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        mySet = set()
        i = 0

        while i < len(word):
            char = word[i]
            if char.isdigit():
                while i < len(word) and word[i] == "0":
                    i += 1
                j = i
                while i < len(word) and word[i].isdigit():
                    i += 1
                print(word[j:i])
                mySet.add(word[j:i])
            else:
                i += 1
        
        return len(mySet)
                
            

        
        