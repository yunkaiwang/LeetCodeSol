class Solution(object):
    def compareVersion(self, version1, version2):
        cur_v1, cur_v2 = "", ""
        while version1 or version2:
            i = 0
            while i < len(version1) and version1[i] != ".":
                i += 1
            cur_v1 = int(version1[:i]) if version1 else 0
            version1 = version1[i+1:]
            
            i = 0
            while i < len(version2) and version2[i] != ".":
                i += 1
            cur_v2 = int(version2[:i]) if version2 else 0
            version2 = version2[i+1:]
            
            if cur_v1 < cur_v2:
                return -1
            elif cur_v1 > cur_v2:
                return 1
        return 0