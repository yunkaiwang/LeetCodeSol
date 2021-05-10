class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [-1] * (n - 2)

        for i in range(2, n):
            if prime[i - 2] != -1:
                continue  # has been visited
            else:
                prime[i - 2] = 1
                curr = i * 2
                while curr < n:
                    prime[curr - 2] = 0
                    curr += i
        return sum(prime)