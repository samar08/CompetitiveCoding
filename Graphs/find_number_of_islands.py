class Solution:
    def bfs(self, x, y, n, m, grid):
        if (x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == '0'):
            return
        grid[x][y] = '0'
        self.bfs(x + 1, y, n, m, grid)
        self.bfs(x, y + 1, n, m, grid)
        self.bfs(x - 1, y, n, m, grid)
        self.bfs(x, y - 1, n, m, grid)
        # self.bfs(x+1,y+1,n,m,grid)
        # self.bfs(x-1,y-1,n,m,grid)
        # self.bfs(x+1,y-1,n,m,grid)
        # self.bfs(x-1,y+1,n,m,grid)

    def numIslands(self, grid: List[List[str]]) -> int:

        n = len(grid)
        m = len(grid[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if (grid[i][j] == '1'):
                    # print('i,j',i,j)
                    count += 1
                    self.bfs(i, j, n, m, grid)
        return count
