import asyncpraw
import random

reddit_client = asyncpraw.Reddit(
    client_id="id",
    client_secret="secret",
    user_agent="script"
)

class Submission():
    def __init__(self, title="", score=0, link="", nsfw=False, self_txt="", spoiler=False, sub=None):
        self.title = title
        self.score = score
        self.link  = link
        self.nsfw  = nsfw
        self.self_txt = self_txt
        self.spoiler = spoiler
        self.sub = None if not sub else sub.name
    
    def format(self, sub):
        if sub == None: return self

        self.sub = sub.subreddit.display_name
        self.title = sub.title
        self.score = sub.score
        self.link  = sub.permalink
        self.nsfw  = sub.over_18
        self.self_txt = sub.selftext
        self.spoiler = sub.spoiler
        
        if sub.url == sub.permalink: self.url = None
        else: self.url = sub.url

        return self

    def __str__(self):
        return f'Subreddit<r/{self.sub}>{{title: {self.title}, score: {self.score}, link: {self.link}, nsfw: {self.nsfw}, self_txt: {self.self_txt}, spoiler: {self.spoiler}, url: {self.url}}}'


class SubReddit():
    def __init__(self, subreddit: str):
        self.subreddit = subreddit

    async def init(self):
        self.subreddit = await reddit_client.subreddit(self.subreddit)
        return self

    async def get_random_by_hot(self):
        limit = 50
        subrddt = self.subreddit
        subs = []
        async for sub in subrddt.hot(limit=limit):
            subs.append(sub)

        
        chosen_one = random.choice(subs)
        return Submission().format(chosen_one)
   
        

    async def get_random(self, size=1):
        return Submission().format(await self.subreddit.random())


