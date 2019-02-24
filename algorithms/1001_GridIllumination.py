class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        if len(lamps) == 0:
            return [0 for _ in queries]
        lamp_map = {}
        col = {}
        row = {}
        lD = {}
        rD = {}
        
        for lamp in lamps:
            lamp_map[(lamp[0], lamp[1])] = True
            if lamp[1] in col:
                col[lamp[1]] += 1
            else:
                col[lamp[1]] = 1
            if lamp[0] in row:
                row[lamp[0]] += 1
            else:
                row[lamp[0]] = 1
            a = lamp[0]+N-1-lamp[1]
            if a in lD:
                lD[a] += 1
            else:
                lD[a] = 1
            b = lamp[0]+lamp[1]
            if b in rD:
                rD[b] += 1
            else:
                rD[b] = 1
            
        ans = [0 for _ in queries]
        for i, query in enumerate(queries):
            a = query[0]+N-1-query[1]
            b = query[0]+query[1]
            if (query[1] in col and col[query[1]] > 0) or (query[0] in row and row[query[0]] > 0) or (a in lD and lD[a] > 0) or (b in rD and rD[b] > 0):
                ans[i] = 1
            else:
                ans[i] = 0
            
            poses = [(query[0], query[1]), (query[0], query[1]-1),(query[0], query[1]+1),(query[0]-1, query[1]),(query[0]+1, query[1]),(query[0]-1, query[1]-1),(query[0]+1, query[1]+1), (query[0]-1, query[1]+1), (query[0]+1, query[1]-1)]
            
            for pos in poses:
                if pos in lamp_map and lamp_map[pos] == True:
                    lamp_map[pos] = False
                    col[pos[1]] -= 1
                    row[pos[0]] -= 1
                    lD[pos[0]+N-1-pos[1]] -= 1
                    rD[pos[0]+pos[1]] -= 1
        return ans
        
        
        
        