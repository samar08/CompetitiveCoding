class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = 0
        i = 0
        n = len(height)
        j = n - 1
        while (i < j):
            mini = min(height[i], height[j])
            area = mini * (j - i)
            maxi = max(maxi, area)
            if (height[i] < height[j]):
                i += 1
            else:
                j -= 1
        return maxi
