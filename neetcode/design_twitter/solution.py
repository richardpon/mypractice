class Twitter:

    def __init__(self):
        self.followers: dict[int, set[tuple[int,int]]] = defaultdict(set)
        self.tweets:dict[int, list[int]] = defaultdict(list)
        self.auto_increment = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.auto_increment,tweetId))
        self.tweets[userId] = self.tweets[userId][-10:]
        self.auto_increment += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # get followees + self
        # get all tweets of followees
        # order by auto_increment
        #return most recent 10 tweets without PK

        ids_to_query = [userId] + list(self.followers[userId])

        tweets = set()
        for id_to_query in ids_to_query:
            tweets.update(self.tweets[id_to_query])

        recent_tweets = sorted(list(tweets), key=lambda x: x[0], reverse=True)
        return [tweet[1] for tweet in recent_tweets[:10]]

        
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
        


