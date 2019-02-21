class Solution:
    def fractionToDecimal(self, numerator: 'int', denominator: 'int') -> 'str':
        if not numerator: return "0"
        res = []
        if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0):
            res.append("-")
        
        numerator, denominator = abs(numerator), abs(denominator)
        res.append(numerator // denominator)
        numerator %= denominator
        if not numerator:
            return "".join(map(str, res))
        
        res.append(".")
        dict = {}
        dict[numerator] = len(res)
        while numerator:
            numerator *= 10
            res.append(numerator//denominator)
            numerator %= denominator
            if numerator in dict:
                res.insert(dict[numerator], "(")
                res.append(")")
                break
            else:
                dict[numerator] = len(res)
        return "".join(map(str, res))
        