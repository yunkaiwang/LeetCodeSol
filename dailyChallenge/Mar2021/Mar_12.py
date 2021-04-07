"""
Check If a String Contains All Binary Codes of Size K

Description: Given a bitstring s, find if all binary codes of size k
exist somewhere in s or not

Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11".
They can be all found as substrings at indicies 0, 1, 3 and 2 respectively.

Solution: We use sliding windows for solving this problem.
Time: O(|s|)
Space: O(2^k)
We look at each k-consecutive characters of s, we find the number that
this bitstring of length k represent. We use an array of size 2^k to
keep track of all numbers we have seen, and a number to keep track of
the number of numbers we have not seen so that we don't need to
traverse the array in the end.
"""

class Solution(object):
    def hasAllCodes(self, s, k):
        if len(s) < 2 ** k + k - 1:
            return False

        kPower = 2 ** (k - 1)

        substr = s[:k]
        current_num = 0
        for i in range(k):
            current_num += int(substr[i]) * (2 ** (k - i - 1))

        seen = [False for _ in range(kPower * 2)]
        leftOver = kPower * 2

        for i in range(k, len(s)):
            if seen[current_num] == False:
                leftOver -= 1
                if leftOver == 0:
                    return True
                seen[current_num] = True

            current_num -= kPower * int(substr[0])
            current_num = current_num * 2 + int(s[i])
            substr = substr[1:] + s[i]

        if seen[current_num] == False and leftOver == 1:
            return True
        return False
