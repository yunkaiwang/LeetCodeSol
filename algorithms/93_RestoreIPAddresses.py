class Solution:
    def restoreIpAddresses(self, s):
        if len(s) < 4: return []
        res = []
        
        def dfs(remaining, ip, count):
            if count == 4:
                if not remaining:
                    res.append(ip[1:])
                return
            
            bound = min(len(remaining) + 1, 4)
            for i in range(1, bound):
                if remaining[0] == "0" and i > 1:
                    return
                if int(remaining[:i]) < 256:
                    dfs(remaining[i:], ip + "." + remaining[:i], count+1)
        dfs(s, "", 0)
        return res
        