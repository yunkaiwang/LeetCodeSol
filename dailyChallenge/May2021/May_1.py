class Trie:
    def __init__(self, word="", index=-1):
        self.endingHere = index
        self.indices = []
        self.arr = [None for _ in range(26)]
        self.addWord(word, index)

    def addWord(self, word, index):
        if index > -1:
            self.indices.append(index)

        if not word:
            self.endingHere = index
            return

        if not self.arr[ord(word[0]) - ord('a')]:
            self.arr[ord(word[0]) - ord('a')] = Trie()

        self.arr[ord(word[0]) - ord('a')].addWord(word[1:], index)

    def startWith(self, prefix):
        if not prefix:
            return self.indices
        if not self.arr[ord(prefix[0]) - ord('a')]:
            return []
        return self.arr[ord(prefix[0]) - ord('a')].startWith(prefix[1:])


class WordFilter:

    def __init__(self, words: List[str]):
        uniqueWord = collections.defaultdict(int)
        for i, word in enumerate(words):
            uniqueWord[word] = i

        self.head = Trie()
        for key in uniqueWord:
            self.head.addWord(key, uniqueWord[key])

        self.tail = Trie()
        for key in uniqueWord:
            self.tail.addWord(key[::-1], uniqueWord[key])

    def f(self, prefix: str, suffix: str) -> int:
        l1 = self.head.startWith(prefix)
        l2 = self.tail.startWith(suffix[::-1])
        intersection = sorted(list(set(l1) & set(l2)))

        if intersection:
            return intersection[-1]
        return -1

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)