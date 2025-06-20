from collections import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set) # id mapped to set of all his following id
        self.tweetMap = defaultdict(list) # id with list if of time and tweetId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((-self.time, tweetId))
        self.time += 1 

    def getNewsFeed(self, userId: int) -> List[int]:
        tweetP = self.tweetMap[userId].copy()

        for followingID in self.followMap[userId]:
            tweetP.extend(self.tweetMap[followingID])
        
        heapq.heapify(tweetP)
        res = []
        for i in range(min(10, len(tweetP))):
            res.append(heapq.heappop(tweetP)[1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)