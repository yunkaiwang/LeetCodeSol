class Solution:
    def getPermutation(self, n, k):
        """
        don't like this question, the idea is that based on k, we can know what the first digit of the output will be, what the second digit will be, etc. For instance, if n = 3, then for k <= 2, first digit will be 1, for 2 < k <= 4, second digit will be 2. So we recursively find what the digit should be and then just add them to a string. Best run time 36ms beats 99%
        """
        factorials = [1]
        for i in range(1, n):
            factorials.append(factorials[-1] * (i + 1))
        res = ""
        nums = [i + 1  for i in range(n)]
        
        while nums:
            n -= 1
            digit = nums[(k-1) // factorials[n - 1]]
            nums.remove(digit)
            res += str(digit)
            k = k % factorials[n - 1]
        return res
        