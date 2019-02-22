class Solution:
    def nthUglyNumber(self, n: 'int') -> 'int':
        """
        dynamic programming solution, using O(n) space and O(n) time
        """
        if n < 1: return 0
        dp = [1]
        i2, i3, i5 = 0, 0, 0
        n2, n3, n5 = 2, 3, 5
        for i in range(1, n):
            next = min(n2, n3, n5)
            dp.append(next)
            
            if next == n2:
                i2 += 1
                n2 = dp[i2] * 2
            if next == n3:
                i3 += 1
                n3 = dp[i3] * 3
            if next == n5:
                i5 += 1
                n5 = dp[i5] * 5
        return dp[-1]
            

        """
        Exceed time limit solution, simply increment the counter and current number to find the n-th ugly number (brust force solution)
        """
        if n < 1:
            return 0
        cur_num = 1
        i = 1
        while i < n:
            i += 1
            cur_num += 1
            while not self.isUgly(cur_num):
                cur_num += 1
        return cur_num
        
    def isUgly(self, num: 'int') -> 'bool':
        if num < 1: return False
        while num:
            if num == 1:
                return True
            elif num%2==0:
                num/=2
            elif num%3==0:
                num/=3
            elif num%5==0:
                num/=5
            else:
                return False
        return True