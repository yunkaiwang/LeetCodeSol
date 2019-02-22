class Solution:
    def calculate(self, s: 'str') -> 'int':
        s += "+0"
        lNum, operator, stack = 0, "+", []
        for char in s:
            if char.isdigit():
                lNum = lNum * 10 + int(char)
            else:
                if char == " ":
                    continue
                
                if operator == "+":
                    stack.append(lNum)
                elif operator == "-":
                    stack.append(-lNum)
                elif operator == "/":
                    temp = stack.pop()
                    if temp < 0:
                        stack.append(-(-temp//lNum))
                    else:
                        stack.append(temp//lNum)
                else:
                    stack.append(stack.pop() * lNum)
                
                operator, lNum = char, 0
                
        return sum(stack)