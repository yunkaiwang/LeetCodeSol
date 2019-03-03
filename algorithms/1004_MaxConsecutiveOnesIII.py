class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        # O(n) solution with O(K) space
        maxLength, curLength, flipedIndices = 0, 0, []
        
        for i, a in enumerate(A):
            if a == 1:
                curLength += 1
            else:
                flipedIndices.append(i)
                if len(flipedIndices) > K:
                    l = flipedIndices.pop(0)
                    curLength = i - l
                else:
                    curLength += 1
            maxLength = max(maxLength, curLength)
        return maxLength
        