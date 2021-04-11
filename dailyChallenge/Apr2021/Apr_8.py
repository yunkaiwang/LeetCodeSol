"""
Letter Combinations of a Phone Number

DFS solution
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMap = {'2': ['a', 'b', 'c'],
                     '3': ['d', 'e', 'f'],
                     '4': ['g', 'h', 'i'],
                     '5': ['j', 'k', 'l'],
                     '6': ['m', 'n', 'o'],
                     '7': ['p', 'q', 'r', 's'],
                     '8': ['t', 'u', 'v'],
                     '9': ['w', 'x', 'y', 'z']}

        combinations = []

        def dfs(curComb, digits):
            if not digits:
                if curComb:
                    combinations.append(curComb)
                return

            for digit in letterMap[digits[0]]:
                dfs(curComb + digit, digits[1:])

        dfs("", digits)
        return combinations