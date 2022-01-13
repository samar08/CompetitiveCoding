class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if(len(points)==0):
            return 0
        sp=sorted(points,key=lambda x:x[1])
        pos=sp[0][1]
        n=len(sp)
        arr=1
        for i in range(1,n):
            if(pos>=sp[i][0]):
                continue
            arr+=1
            pos=sp[i][1]
        return arr