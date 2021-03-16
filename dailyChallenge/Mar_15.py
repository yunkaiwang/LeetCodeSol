"""
Design a strategy for tiny URL service

This is simple solution, take sha256 hashing of the long url,
use the first several digit as hashcode and the shortened url,
store these information in a hashmap.

Will create conflict in hashmap if the two hash code have the
same starting digits.
Possible solution can be use two different hash functions and
multiple hashmaps.
The first hash function decides which hashmap we will store
the url, the second hash function does exactly what we just
described. However, this will still not solve the problem
completely since there is still a tiny chance that the two
url will have the same result for both hash functions. But
there is no way one can solve this problem completely.
"""

from hashlib import sha256

class Codec:
    def __init__(self):
        self.map = {}

    def encode(self, longUrl):
        hashcode = sha256(longUrl.encode("utf-8")).hexdigest()[:5]
        self.map[hashcode] = longUrl
        return hashcode

    def decode(self, shortUrl):
        if shortUrl in self.map:
            return self.map[shortUrl]
        return None

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))