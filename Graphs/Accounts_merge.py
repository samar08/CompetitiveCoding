class Solution:
    def buildgraph(self, g, emailtoname, accounts):
        for a in accounts:
            name = a[0]
            for i in range(1, len(a)):
                emailtoname[a[i]] = name
                if (a[i] not in g):
                    g[a[i]] = set()
                if (i == 1):
                    continue
                prev = a[i - 1]
                g[prev].add(a[i])
                g[a[i]].add(prev)

    def dfs(self, key, g, lis, vis):
        if (len(g[key]) == 0):
            return
        for neigh in g[key]:
            if (neigh not in vis):
                vis.add(neigh)
                lis.append(neigh)
                self.dfs(neigh, g, lis, vis)

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        g = {}
        emailtoname = {}
        self.buildgraph(g, emailtoname, accounts)
        vis = set()
        res = []
        for key in emailtoname:

            if (key not in vis):
                vis.add(key)
                lis = []
                lis.append(key)
                self.dfs(key, g, lis, vis)
                lis.sort()
                lis.insert(0, emailtoname[key])
                res.append(lis)
        return res

#         n=len(accounts)
#         ac=[]
#         for i in range(n):
#             setac=set(accounts[i][1:])
#             ac.append([accounts[i][0],setac])
#         vis=[0 for i in range(n)]
#         for i in range(n-1,-1,-1):

#             for val in ac[i][1]:
#                 for j in range(i-1,-1,-1):
#                     if(val in ac[j][1]):
#                         vis[i]=1
#                         ac[j][1].update(ac[i][1])
#         #print(ac)
#         out=[]
#         #print(vis)
#         for i in range(n):
#             if(vis[i]==0):
#                 mat=[ac[i][0]]
#                 arr=list(ac[i][1])
#                 arr.sort()
#                 for v in arr:
#                     mat.append(v)
#                 out.append(mat)
#         return out






