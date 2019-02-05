class Solution:
    def numTrees(self, n):
        if not n: return 0
        self.pre_calculated = [0 for _ in range(n)]
        return self.dfs(n)
    
    def dfs(self, n):
        if not n:
            return 1
        elif self.pre_calculated[n - 1]:
            return self.pre_calculated[n - 1]
        
        total = 0
        for i in range(n):
            left_count = self.dfs(i)
            right_count = self.dfs(n-1-i)
            total += left_count * right_count
        self.pre_calculated[n - 1] = total
        return total
        