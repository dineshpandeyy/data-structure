'''
Problem Statement #
There is a dictionary containing words from an alien language for which we don’t know the ordering of the characters. Write a method to find the correct order of characters in the alien language.

Example 1:

Input: Words: ["ba", "bc", "ac", "cab"]
Output: bac
Explanation: Given that the words are sorted lexicographically by the rules of the alien language, so
from the given words we can conclude the following ordering among its characters:
 
1. From "ba" and "bc", we can conclude that 'a' comes before 'c'.
2. From "bc" and "ac", we can conclude that 'b' comes before 'a'
 
From the above two points, we can conclude that the correct character order is: "bac"
Example 2:

Input: Words: ["cab", "aaa", "aab"]
Output: cab
Explanation: From the given words we can conclude the following ordering among its characters:
 
1. From "cab" and "aaa", we can conclude that 'c' comes before 'a'.
2. From "aaa" and "aab", we can conclude that 'a' comes before 'b'
 
From the above two points, we can conclude that the correct character order is: "cab"
Example 3:

Input: Words: ["ywx", "wz", "xww", "xz", "zyy", "zwz"]
Output: ywxz
Explanation: From the given words we can conclude the following ordering among its characters:
 
1. From "ywx" and "wz", we can conclude that 'y' comes before 'w'.
2. From "wz" and "xww", we can conclude that 'w' comes before 'x'.
3. From "xww" and "xz", we can conclude that 'w' comes before 'z'
4. From "xz" and "zyy", we can conclude that 'x' comes before 'z'
5. From "zyy" and "zwz", we can conclude that 'y' comes before 'w'
 
From the above five points, we can conclude that the correct character order is: "ywxz"

'''

from collections import defaultdict, deque
def foreignDictionary(words):
    if not words:
        return ""
    
    in_degree = defaultdict(int)
    graph = defaultdict(list)


    for word in words:
        for char in word:
        # Ensure every character is in the graph
            in_degree[char] = 0

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))
        for j in range(min_len):
            parent, child = w1[j], w2[j]
            if parent != child:
                graph[parent].append(child)
                in_degree[child] += 1
                break
        else:
            # Edge case: ["abc", "ab"] is invalid ordering
            if len(w1) > len(w2):
                return ""
    
    sources = deque([])
    for char in in_degree:
        if in_degree[char] == 0:
            sources.append(char)
    

    sorted_order = []
    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

# Step e: Check for cycles
    if len(sorted_order) != len(in_degree):
        return ""

    return ''.join(sorted_order)

Words = ["ba", "bc", "ac", "cab"]
print(foreignDictionary(Words))
Words = ["cab", "aaa", "aab"]
print(foreignDictionary(Words))
Words = ["ywx", "wz", "xww", "xz", "zyy", "zwz"]
print(foreignDictionary(Words))
