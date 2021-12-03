class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if (n == 1):
            return nums[0]
        maxi = nums[0]
        mini = nums[0]
        ans = maxi
        for i in range(1, n):
            if (nums[i] >= 0):
                maxi = max(maxi * nums[i], nums[i])
                mini = min(mini * nums[i], nums[i])
            else:
                temp = maxi
                maxi = mini
                mini = temp
                maxi = max(maxi * nums[i], nums[i])
                mini = min(mini * nums[i], nums[i])
            ans = max(maxi, ans)
        return ans


