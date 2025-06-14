from collections import defaultdict
def longestPalindrome(words):
    maps = defaultdict(int)
    result = 0

    for char in words:
        if char[::-1] in maps:
            result += 4
            maps[char[::-1]] -= 1
            if maps[char[::-1]] == 0:
                del maps[char[::-1]]
        else:
            maps[char] += 1
    
    # we can use word with same character only for 
    # the one time in the middle if we didn't find the reversed of that
    for key in maps.keys():
        if key[0] == key[1]:
            result += 2
            break
    
    return result

words = ["lc","cl","gg"]
# Output: 6
print(longestPalindrome(words))


'''
Use a hash map to count word frequencies and efficiently find reversed pairs.
Different-character words (e.g., "AB") pair with their reverses ("BA") to add 4 to the palindrome length. Decrement their counts.
Same-character words (e.g., "AA") can only be used once in the middle, adding 2 to the length.
First, process all reverse pairs, then check for a single middle word with identical characters.
'''