class Solution:
	def setBits(self, N):
		# code here
		count=0
		while(N>0):
		    if(N&1==1):
		        count+=1
		    N=N>>1
		return count