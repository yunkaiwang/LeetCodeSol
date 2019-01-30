class Solution:
    def simplifyPath(self, path):
        """
        don't like this question, how can a directory be named as ...? Really annoying question. Two solutions provided, one constantly building the path, the other one uses a stack(to make poping last file index faster), using stack is faster, but no siganificantly faster.
        """
        res = "/"
        i = 0
        while i < len(path):
            if path[i] == "/":
                if res[-1] != "/":
                    res = res + "/"
            elif path[i] == ".":
                
                met_other = False
                count = 1
                while count + i < len(path) and path[i + count] != "/":
                    if path[i+count] != ".":
                        met_other = True
                    count += 1
                if count > 2 or met_other:
                    res += path[i:i+count]
                    i += count - 1
                elif count == 2:
                    prev = len(res) - 1
                    while prev - 1 > -1 and res[prev-1] != "/":
                        prev -= 1
                    res = res[:prev] if prev != 0 else res
            else:
                res = res + path[i]
            i += 1
        return res if res[-1] != "/" or res == "/" else res[:-1]
        
        """solution using stack"""
        stack = []
        i = 0
        c = ""
        while i < len(path):
            if path[i] == "/":
                if c == "..":
                    if stack:
                        stack.pop()
                elif c and c != ".":
                    stack.append(c)
                c = ""
            else:
                c += path[i]
            i += 1
        if c:
            if c == "..":
                if stack:
                    stack.pop()
            elif c != ".":
                    stack.append(c)
        return "/" + "/".join(stack)