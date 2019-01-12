class Solution:
    def letterCombinations(self, digits):
        """
        two solutions provided, one DFS solution and the other one simply use 3 for loops
        """
        if len(digits) <= 0:
            return []
        mapping = {'2': ['a', 'b', 'c'],
                   '3': ['d', 'e', 'f'],
                   '4': ['g', 'h', 'i'],
                   '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'],
                   '7': ['p', 'q', 'r', 's'],
                   '8': ['t', 'u', 'v'],
                   '9': ['w', 'x', 'y', 'z']}
        
        # sol 1
        res = [""]
        for digit in digits:
            res = [str + char for str in res for char in mapping[digit]]
        
        
        # sol 2
        res = []
        def dfs(digits, index, cur):
            if index == len(digits):
                res.append(cur)
                return
            else:
                for char in mapping[digits[index]]:
                    dfs(digits, index + 1, cur + char)
        
        dfs(digits, 0, '')
        return res