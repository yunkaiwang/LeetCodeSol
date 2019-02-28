class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        def helper(index, curOp, lastOp, curSum, equation):
            if index == len(num):
                if curSum == target and curOp == 0:
                    res.append(equation[1:])
            else:
                curOp = curOp*10 + int(num[index])
                
                if curOp > 0:
                    helper(index+1, curOp, lastOp, curSum, equation)
                    
                helper(index+1,0,curOp,curSum+curOp,equation+"+"+str(curOp))
                if equation:
                    helper(index+1,0, -curOp,curSum-curOp,equation+"-"+str(curOp))
                    product = curOp*lastOp
                    helper(index+1,0,product,curSum-lastOp+product,equation+"*"+str(curOp))
        helper(0, 0, 0, 0, "")
        return res
                
        
        