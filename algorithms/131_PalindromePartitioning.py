class Solution:
    def partition(self, s: 'str') -> 'List[List[str]]':
        def isPalindrome(s):
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        partitions = []
        def dfs(left_s, cur_list):
            if not left_s:
                partitions.append(cur_list)
            
            for i in range(len(left_s)):
                if isPalindrome(left_s[:i+1]):
                    dfs(left_s[i+1:], cur_list+[left_s[:i+1]])
        
        dfs(s, [])
        return partitions

        """ use hashmap to store checked strings, running slower than the previous solution without using hashmap, but this should run faster for longer strings
        def isPalindrome(s):
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        partitions = []
        rem = {}
        def dfs(left_s, cur_list):
            if not left_s:
                partitions.append(cur_list)
            
            for i in range(len(left_s)):
                if (left_s[:i+1] in rem and rem[left_s[:i+1]]) or (not left_s[:i+1] in rem and isPalindrome(left_s[:i+1])):
                    rem[left_s[:i+1]] = True
                    dfs(left_s[i+1:], cur_list+[left_s[:i+1]])
                else:
                    rem[left_s[:i+1]] = False
        
        dfs(s, [])
        return partitions
        """

        