nums=list(map(int,input().split(' ')))
ca=int(input())
cb=int(input())
xa=ca
xb=cb
n=len(nums)
i=0
j=n-1
refil=0
while(i<=j):
    if(i==j):
        if(xa>=xb):
            if(xa<nums[i]):
                refil+=1
                xa=ca
                xa-=nums[i]
            else:
                xa-=nums[i]
        else:
            if(xb<nums[i]):
                refil+=1
                xb=cb
                xb-=nums[i]
            else:
                xb-=nums[i]
        i+=1
        j-=1
    else:
        if(xa<nums[i]):
            refil+=1
            xa=ca
            xa-=nums[i]
        elif(xa>=nums[i]):
            xa-=nums[i]

        if(xb<nums[j]):
            refil+=1
            xb=cb
            xb-=nums[j]
        elif(xb>=nums[j]):
            xb-=nums[j]
        i+=1
        j-=1
print(refil)
            
        
