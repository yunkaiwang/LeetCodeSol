class Solution:
    def letterCombinations(self, digits):
        if not digits: return []
        mapping = {'2': ['a', 'b', 'c'],
                   '3': ['d', 'e', 'f'],
                   '4': ['g', 'h', 'i'],
                   '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'],
                   '7': ['p', 'q', 'r', 's'],
                   '8': ['t', 'u', 'v'],
                   '9': ['w', 'x', 'y', 'z']}
        sol = []
        def dfs(combination, digits):
            if not digits:
                sol.append(combination)
            else:
                for map in mapping[digits[0]]:
                    dfs(combination + map, digits[1:])
        
        dfs("", digits)
        return sol