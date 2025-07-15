class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowelLetter = {"a", "e", "i", "o", "u"}
        vowel = False
        consonant = False
        digit = False

        for char in word:
            if not char.isalnum():
                return False
            
            elif char.lower() in vowelLetter:
                vowel = True
            elif not char.lower() in vowelLetter and char.isalpha():
                consonant = True
        
        return vowel and consonant


# UuE6      
            



    