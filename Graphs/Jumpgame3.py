class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        vis = [0 for i in range(n)]
        return self.dfs(start, arr, vis, n)

    def dfs(self, st, arr, vis, n):
        if (st < 0 or st >= n):
            return False
        if (vis[st] == 0):
            vis[st] = 1
            if (arr[st] == 0):
                return True
            else:
                return (self.dfs(st + arr[st], arr, vis, n) or self.dfs(st - arr[st], arr, vis, n))

        else:
            return False