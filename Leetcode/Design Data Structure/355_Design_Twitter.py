import heapq
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set) # followId map to set of followingID
        self.tweetMap = defaultdict(list) # id map to list of [(time, tweetId)]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followingIdSet = self.followMap[userId] | {userId} # set of following ID
        heap = [] # list of (time, id)

        for followID in followingIdSet:
            for timeAndTweetID in self.tweetMap[followID][-10:]:
                heapq.heappush(heap, timeAndTweetID)
            
                if len(heap) > 10:
                    heapq.heappop(heap)
            
        res = []
        for t, TweetID in sorted(heap):
            res.append(TweetID)
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