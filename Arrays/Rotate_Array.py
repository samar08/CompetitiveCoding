class Solution:
    def swap(self, A, i, j):

        data = A[i]
        A[i] = A[j]
        A[j] = data

    # Function to reverse a given sublist
    def reverse(self, A, low, high):
        i = low
        j = high
        while i < j:
            self.swap(A, i, j)
            i = i + 1
            j = j - 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if (k == 0):
            return
        self.reverse(nums, n - k, n - 1)

        # Reverse the first `n-k` elements
        self.reverse(nums, 0, n - k - 1)

        # Reverse the whole list
        self.reverse(nums, 0, n - 1)

        # nums.reverse()
        # self.reverse_sublist(nums,0,k)
        # print(nums)
        # self.reverse_sublist(nums,k,n)
        # print(nums)
        # a=nums[n-k:]
        # b=nums[0:n-k]
        # nums=a+b
        # print(a)
        # print(b)
        # print(nums)
        # for j in range(k):
        #     x=nums[n-1]
        #     for i in range(n-1,0,-1):
        #         #temp=nums[i]
        #         nums[i]=nums[i-1]
        #     nums[0]=x




