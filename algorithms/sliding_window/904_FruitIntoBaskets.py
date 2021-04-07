"""
Two pass with constant extra space
"""
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        maxFruit, i = 0, 0
        window = collections.Counter()
        for j, f in enumerate(tree):
            window[f] += 1
            while len(window) > 2:
                window[tree[i]] -= 1
                if window[tree[i]] == 0:
                    del window[tree[i]]
                i += 1
            maxFruit = max(maxFruit, j-i+1)
        return maxFruit