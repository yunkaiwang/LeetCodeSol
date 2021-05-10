class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        xPowers = [1]  # list of power of x that is smaller than bound
        if x > 1:  # when x = 1, this will create an infinite loop, so take care of that case
            cur = x
            while cur < bound:
                xPowers.append(cur)
                cur *= x

        res = set()
        if y > 1:
            cur = 1
            while cur < bound:
                for num in xPowers:
                    if cur + num <= bound:
                        res.add(cur + num)
                    else:
                        break
                cur *= y
        else:  # take care of the case when y = 1
            for num in xPowers:
                if 1 + num <= bound:
                    res.add(1 + num)
                else:
                    break
        return res