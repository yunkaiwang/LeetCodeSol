class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        lcp, i = "", 0
        while i < len(strs[0]):
            char = strs[0][i]
            for s in strs[1:]:
                if i < len(s) and s[i] == char:
                    continue
                else:
                    return lcp
            lcp += char
            i += 1
        return lcp