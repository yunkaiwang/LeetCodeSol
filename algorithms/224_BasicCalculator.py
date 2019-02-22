class Solution:
    def calculate(self, s: 'str') -> 'int':
        cur_s = []
        for i, char in enumerate(s):
            if char == " ":
                continue
            elif char.isdigit():
                if cur_s and isinstance(cur_s[-1], int):
                    temp = cur_s.pop()
                    temp *= 10
                    temp += int(char)
                    cur_s.append(temp)
                else:
                    cur_s.append(int(char))
            elif char in ["(", "+", "-"]:
                cur_s.append(char)
            elif char == ")":
                ans = 0
                while cur_s[-1] != "(":
                    temp = cur_s.pop()
                    if cur_s[-1] == "+":
                        cur_s.pop()
                    elif cur_s[-1] == "-":
                        cur_s.pop()
                        temp = -temp
                    ans += temp
                cur_s.pop()
                cur_s.append(ans)
                
        ans = 0
        while cur_s:
            temp = cur_s.pop()
            if cur_s and cur_s[-1] == "+":
                cur_s.pop()
            elif cur_s and cur_s[-1] == "-":
                cur_s.pop()
                temp = -temp
            ans += temp
        return ans
                    
            