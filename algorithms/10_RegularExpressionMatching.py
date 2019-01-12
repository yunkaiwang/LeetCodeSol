class Solution:
    def isMatch(self, s, p):
        # easy to understand DP solution, but it takes O(len(s) * len(p)) times, and the same amount of space
        table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]

        table[0][0] = True
        
        for i in range(2, len(p) + 1):
            table[i][0] = table[i - 2][0] and p[i - 1] == '*'

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] != "*":
                    table[i][j] = table[i - 1][j - 1] and \
                                  (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                else:
                    table[i][j] = table[i - 2][j] or table[i - 1][j]
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        table[i][j] |= table[i][j - 1]

        return table[-1][-1]
        
        
        """
        I have another idea of solving this problem, with code listed below, the code still has problems that need to be fixed as it still fails the test, I tried to fix it but I have no luck finishing it since the DP solution is very obvious. The second idea runs in linear time in the size of s and p, so they will loop through s and p exactly once, but there are too many cases to be considered, for instance, if s is 'aab', and p is 'a*b*ab', then the algorithm need to figure out that the first 'a*' should only match 'a', not 'aa', so the actual solution(if finished), should be very complicated and hard to understand, but it's a good reference so that I copied them below.
        """
#         prev_match_char, curr_pattern_index, curr_string_index, prev_count = "", 0, 0, 0
#         str_len = len(s)
#         pat_len = len(p)
        
#         while curr_pattern_index < pat_len: # read until the match pattern string end
#             char = s[curr_string_index] if curr_string_index < str_len else ""
#             match_char = p[curr_pattern_index]
#             match_any_char = True if match_char == "." else False # current match character is ., so match any character
#             if curr_pattern_index < pat_len - 1 and p[curr_pattern_index + 1] == "*": # next character is *
#                 curr_pattern_index += 2
                
#                 # match 0 or more of the character
#                 while char == match_char or match_any_char:
#                     prev_count += 1
#                     prev_match_char = char
#                     curr_string_index += 1
#                     if not curr_string_index < str_len:
#                         break
#                     char = s[curr_string_index]
#             else:
#                 if prev_count > 0 and (match_char == prev_match_char or match_char=="."):
#                     curr_count = 0
#                     while curr_pattern_index < pat_len:
#                         if p[curr_pattern_index] == prev_match_char or p[curr_pattern_index] == ".":
#                             curr_count += 1
#                             curr_pattern_index += 1
#                             continue
#                         break
#                     if prev_count > 0 and curr_count > prev_count:
#                         print("case 1", curr_count, prev_count)
#                         return False
#                 else:
#                     if not (match_any_char or char==match_char):
#                         print("case 2", "-", char, "-", match_char)
#                         return False

#                     prev_count = 0
#                     curr_string_index += 1
#                     curr_pattern_index += 1
            
#         # we have reached the end of the match string but not the input string, so they don't match
#         if curr_string_index < str_len:
#             print("Case3", curr_string_index, str_len)
#             return False
        
#         return True # everying matches, so return True
        