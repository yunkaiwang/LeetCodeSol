"""
Stamping the sequence

O(m^2 n) solution
"""
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n, m = len(stamp), len(target)
        visited = [False] * len(target)
        targetArr = list(target)
        ans = []
        star = 0

        while star < len(target):
            madeChange = False

            for i in range(m - n + 1):
                match = 0
                if visited[i]:
                    continue
                for j in range(n):
                    if targetArr[i + j] == '.' or targetArr[i + j] == stamp[j]:
                        match += 1
                if match == n:
                    madeChange = True
                    ans.append(i)
                    visited[i] = True
                    for j in range(n):
                        if targetArr[i + j] != '.':
                            star += 1
                        targetArr[i + j] = '.'

            if not madeChange:
                return []

        return ans[::-1]
