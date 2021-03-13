"""
Binary Trees With Factors

Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number may be used for any number of times.
Each non-leaf node's value should be equal to the product of the values of its children.

Input: arr = [2,4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]

Solution: Dynamic programming problem
Time: O(n^2)
Space: O(n)
"""
class Solution(object):
    def numFactoredBinaryTrees(self, arr):

        number_dic = {}
        for num in arr:
            number_dic[num] = []

        arr.sort()
        for i, num in enumerate(arr):
            for j in range(i, len(arr)):
                num2 = arr[j]
                product = num * num2
                if product in number_dic:
                    number_dic[product].append((i, j))

        dp = [1 for _ in arr]

        for i, num in enumerate(arr):
            for (index1, index2) in number_dic[num]:
                if index1 == index2:
                    dp[i] = dp[i] + dp[index1] * dp[index2]
                else:
                    dp[i] = dp[i] + 2 * (dp[index1] * dp[index2])

        return sum(dp) % (10 ** 9 + 7)