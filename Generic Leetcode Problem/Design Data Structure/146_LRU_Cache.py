'''
146. LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair
 to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
'''
from collections import OrderedDict
class Solution:
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self,key):
        if key in self.cache:
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
            return value
        return -1

    def put(self,key, value):
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = value
        if len(self.cache) >  self.capacity:
            self.cache.popitem(last=False)
        

lRUCache = Solution(2);
lRUCache.put(1, 1); 
lRUCache.put(2, 2); 
print(lRUCache.get(1));   
lRUCache.put(3, 3); 
print(lRUCache.get(2));    
lRUCache.put(4, 4); 
print(lRUCache.get(1));    
print(lRUCache.get(3));    
print(lRUCache.get(4));    
        

