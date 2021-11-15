class Solution:
    def bfs(self, i, j, n, m, grid, vis):
        if (i < 0 or i >= n or j < 0 or j >= m or vis[i][j] == 1 or grid[i][j] == 0):
            return False
        vis[i][j] = 1
        if (grid[i][j] == 2):
            return True
        return (self.bfs(i + 1, j, n, m, grid, vis) or self.bfs(i, j + 1, n, m, grid, vis) or self.bfs(i - 1, j, n, m,
                                                                                                       grid,
                                                                                                       vis) or self.bfs(
            i, j - 1, n, m, grid, vis))

        def is_Possible(self, grid):
            # Code here
            n = len(grid)
            m = len(grid[0])
            vis = []
            for i in range(n):
                mat = []
                for j in range(m):
                    mat.append(0)
                vis.append(mat)

            for i in range(n):
                for j in range(m):
                    if (grid[i][j] == 1):
                        return self.bfs(i, j, n, m, grid, vis)