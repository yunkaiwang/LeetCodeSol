class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        reading0, cons1, cons0 = False, 0, 0

        for c in s:
            if c == '1':
                if reading0:
                    cons1 = 0
                reading0 = False
                cons1 += 1
                if cons1 <= cons0:
                    count += 1
            else:
                if not reading0:
                    cons0 = 0
                reading0 = True
                cons0 += 1
                if cons0 <= cons1:
                    count += 1
        return count
