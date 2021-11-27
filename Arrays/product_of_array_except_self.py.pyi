class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        left = [0 for i in range(n)]
        right = [0 for i in range(n)]
        pre = 1
        post = 1
        out = [0 for i in range(n)]
        for i in range(n):
            pre = pre * nums[i]
            left[i] = pre
        for i in range(n - 1, -1, -1):
            post = post * nums[i]
            right[i] = post
        for i in range(n):
            if (i == 0):
                out[i] = right[i + 1]
            elif (i == n - 1):
                out[i] = left[i - 1]
            else:
                out[i] = left[i - 1] * right[i + 1]
        return out



