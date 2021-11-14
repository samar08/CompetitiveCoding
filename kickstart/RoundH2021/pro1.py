def left(i,dp):
    orda=ord('a')
    cp=ord(i)-orda
    l=(cp-1)%26
    count=1
    while(dp[l]!=1):
        l=(l-1)%26
        count+=1
    return count


def right(i,dp):
    orda=ord('a')
    cp=ord(i)-orda
    r=(cp+1)%26
    count=1
    while(dp[r]!=1):
        r=(r+1)%26
        count+=1
    return abs(count)
    
t=int(input())
for te in range(t):
    s=input().rstrip()
    f=input().rstrip()
    lf=len(f)
    ls=len(s)
    ds={}
    orda=ord('a')
    for i in s:
        if i in ds:
            ds[i]+=1
        else:
            ds[i]=1
    out=0
    #sf=set(f)
    dp=[0 for i in range(26)]
    for i in range(lf):
        dp[ord(f[i])-orda]=1
    for i in (ds):
        if(dp[ord(i)-orda]==0):
            l=left(i,dp)
            r=right(i,dp)
            #print('l,r', l,r)
            out+=min(l,r)*ds[i]
            #print(out)
            
            
    
    



    print('Case #'+str(te+1)+": "+str(out))
