class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.users = defaultdict(set)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None: 
        self.tweets[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.users[userId].add(userId)
        relevantTweets = []
        for followeeId in self.users[userId]:
            relevantTweets += self.tweets[followeeId]
        heapq.heapify(relevantTweets)
        res = []
        i = 0
        while i < 10 and relevantTweets:
            publishedTime, tweetId = heapq.heappop(relevantTweets)
            res.append(tweetId)
            i += 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.users[followerId].discard(followeeId)