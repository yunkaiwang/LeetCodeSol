class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # just to make sure we use minimum possible space
        if m < n:
            word1, word2, m.n = word2, word1, n, m

        # O(mn) space solution
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i

        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                cross = dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    cross += 1

                add = dp[i - 1][j] + 1
                delete = dp[i][j - 1] + 1
                dp[i][j] = min(add, delete, cross)

        # O(2 * min(m, n)) space solution
        dp2 = [0] * (n + 1)
        for j in range(n + 1):
            dp2[j] = j
        for i in range(1, m + 1):
            next = [i] + [0] * (n)
            for j in range(1, n + 1):
                cross = dp2[j - 1]
                if word1[i - 1] != word2[j - 1]:
                    cross += 1
                add = dp2[j] + 1
                delete = next[j - 1] + 1
                next[j] = min(cross, add, delete)
            dp2 = next

        # O(min(m, n)) space solution
        dp3 = [0] * (n + 1)
        for j in range(n + 1):
            dp3[j] = j
        for i in range(1, m + 1):
            prev = dp3[0]
            dp3[0] = i
            for j in range(1, n + 1):
                temp = dp3[j]
                cross = prev
                if word1[i - 1] != word2[j - 1]:
                    cross += 1

                add = dp3[j] + 1
                delete = dp3[j - 1] + 1
                dp3[j] = min(cross, add, delete)
                prev = temp

        return dp3[-1]