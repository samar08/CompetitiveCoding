class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        n=len(time)
        rem=[0 for i in range(60)]
        for i in range(n):
            rem[time[i]%60]+=1
        count=0
        count+=((rem[0]*(rem[0]-1))//2)
        count+=((rem[30]*((rem[30]-1)))//2)
        for i in range(1,30):
            count+=rem[i]*(rem[60-i])
        return count