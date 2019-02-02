class Solution:
    def isScramble(self, s1, s2):
        """
        you just have to recursively compare all the possible cases, and the question is not clear about how we can split the string, bad question
        """
        memo = {}
        
        def helper(s1, s2):
            if not s1 or not s2: return False
            if s1 == s2: return True
            if sorted(s1) != sorted(s2): return False
            
            if (s1, s2) in memo: return memo[s1,s2]
            
            ans = False
            for i in range(len(s1)):
                if ((helper(s1[:i], s2[:i]) and helper(s1[i:], s2[i:])) or
                (helper(s1[:i], s2[-i:]) and helper(s1[i:], s2[:-i]))):
                    ans = True
                    break

            memo[(s1, s2)] = ans
            return ans
        
        return helper(s1, s2)