class Solution:

    # Function to detect cycle in an undirected graph.
    def isCycle(self, V, adj):
        # Code here
        vis = [0 for i in range(V)]
        rec = [0 for i in range(V)]
        for i in range(V):
            if (self.dfs(i, vis, rec, adj) == True):
                return True
        return False

    def dfs(self, i, vis, rec, adj):
        if (rec[i] == 1):
            return True
        if (vis[i] == 1):
            return False

        vis[i] = 1
        rec[i] = 1
        for j in range(len(adj[i])):

            if (self.dfs(adj[i][j], vis, rec, adj) == True):
                return True
        rec[i] = 0
        return False