class Solution(object):
    def accountsMerge(self, accounts):
        graph = collections.defaultdict(list)
        email_name = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_name[email] = name

                graph[email].append(account[1])
                graph[account[1]].append(email)

        visited = set()
        sol = []
        for email in email_name.keys():
            l = []
            if email not in visited:
                stack = [email]
                while stack:
                    curr = stack.pop()
                    if curr not in visited:
                        l.append(curr)
                        visited.add(curr)
                        stack += graph[curr]

                sol.append([email_name[email]] + sorted(l))

        return sol