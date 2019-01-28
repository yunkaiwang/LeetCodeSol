class Solution:
    def fullJustify(self, words, maxWidth):
        """
        very annoying question, not so useful, but here is a solution that runs in 32ms and beats 100%
        """
        res = []
        
        i, c_l, c_c, c_g = 0, 0, 0, []
        while i < len(words):
            c_l, c_c, c_g = 0, 0, []
            while i < len(words) and c_l + c_c + len(words[i]) <= maxWidth:
                c_g.append(words[i])
                c_c += 1
                c_l += len(words[i])
                i += 1
            
            n_w = maxWidth - c_l
            if i < len(words):
                if c_c < 2:
                    res.append(c_g[0] + " " * n_w)
                else:
                    while n_w >= c_c - 1:
                        c_g = [c_g[i] + " " for i in range(c_c - 1)] + [c_g[-1]]
                        n_w -= c_c - 1
                    c_g = [c_g[i] + " " for i in range(n_w)] + c_g[n_w:]
                    res.append("".join(c_g))
            else:
                res.append(" ".join(c_g) + " " * (n_w - (c_c - 1)))
        return res
            
        