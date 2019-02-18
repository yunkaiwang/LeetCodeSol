class Solution(object):
    def reverseWords(self, s):
        reverse_string = ""
        
        current_i = len(s) - 1
        while current_i >= 0:
            while current_i >= 0 and s[current_i] == " ":
                current_i -= 1
            
            current_word = ""
            while current_i >= 0 and s[current_i] != " ":
                current_word = s[current_i] + current_word
                current_i -= 1
            
            if current_word:
                reverse_string += current_word + " "
        return reverse_string[:-1]