class Solution:
    def singleNumber(self, arr):

    # Code here
    # 		j=nums[0]
    # 		n=len(nums)

    # 		for i in range(1,n):
    # 		    j=j^nums[i]
    # 		right=j&(~(j-1))
    # 		x=y=0
    # 		for i in nums:
    # 		    if(right&i==1):
    # 		        x=x^i
    # 		    else:
    # 		        y=y^i
    # 		out=[x,y]
    # 		out.sort()
    # 		return out
    sums = 0
    n = len(arr)
    for i in range(0, n):
        # Xor  all the elements of the array
        # all the elements occurring twice will
        # cancel out each other remaining
        # two unique numbers will be xored
        sums = (sums ^ arr[i])

    # Bitwise & the sum with it's 2's Complement
    # Bitwise & will give us the sum containing
    # only the rightmost set bit
    sums = (sums & -sums)

    # sum1 and sum2 will contains 2 unique
    # elements elements initialized with 0 box
    # number xored with 0 is number itself
    sum1 = 0
    sum2 = 0

    # Traversing the array again
    for i in range(0, len(arr)):

        # Bitwise & the arr[i] with the sum
        # Two possibilities either result == 0
        # or result > 0
        if (arr[i] & sums) > 0:

            # If result > 0 then arr[i] xored
            # with the sum1
            sum1 = (sum1 ^ arr[i])

        else:

            # If result == 0 then arr[i]
            # xored with sum2
            sum2 = (sum2 ^ arr[i])
    out = [sum1, sum2]
    out.sort()
    return out