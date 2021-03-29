"""
Word Subsets

O(m+n) solution.
"""
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        AMapList = [collections.Counter(word) for word in A]
        BMap = collections.defaultdict(int)
        for word in B:
            wordCount = collections.Counter(word)
            for key in wordCount.keys():
                BMap[key] = max(BMap[key], wordCount[key])
        universal = []

        for i in range(len(A)):
            match = True
            for key in BMap.keys():
                if key not in AMapList[i] or BMap[key] > AMapList[i][key]:
                    match = False

            if match:
                universal.append(A[i])
        return universal