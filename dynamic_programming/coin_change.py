class Solution:
    def solve(self, index, amount, coins, n, dp):
        if (amount == 0):
            return 1
        if (index >= n or coins[index] > amount):
            return 0
        if (dp[index][amount] != -1):
            return dp[index][amount]
        dp[index][amount] = self.solve(index, amount - coins[index], coins, n, dp) + self.solve(index + 1, amount,
                                                                                                coins, n, dp)
        return dp[index][amount]

    def change(self, amount: int, coins: List[int]) -> int:
        dp = []
        n = len(coins)
        coins.sort()
        for i in range(n):
            mat = []
            for j in range(amount + 1):
                mat.append(-1)
            dp.append(mat)
        return self.solve(0, amount, coins, n, dp)
