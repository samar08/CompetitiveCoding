import sys
nums=list(map(int,input().split(" ")))
n=len(nums)
#mini=sys.maxsize()
#maxi=-sys.maxsize()
count=0
for i in range(n):
    mini=nums[i]
    maxi=nums[i]
    for j in range(i+1,n):
        mini=min(mini,nums[j])
        maxi=max(maxi,nums[j])
        count+=(maxi-mini)
print(count)
    
        
        
        
        
