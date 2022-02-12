class Solution:
    def func(self, x, dp, cost):
        if (x > 1):
            if (dp[x] != 0):
                return dp[x]
            else:
                one = self.func(x - 1, dp, cost) + cost[x - 1]
                two = self.func(x - 2, dp, cost) + cost[x - 2]
                dp[x] = min(one, two)
                return dp[x]

        else:
            return 0

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0 for i in range(n + 1)]
        # dp[0]=cost[0]
        # dp[1]=cost[1]
        y = self.func(n, dp, cost)
        # print(dp)
        return dp[n]
