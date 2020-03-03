class User:

    def __init__(self, key, tag, followers = [], rank = 0):
        self.key = key
        self.tag = tag
        self.followers = followers
        self.rank = rank