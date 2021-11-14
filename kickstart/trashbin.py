t=int(input())
for te in range(t):
    n=int(input())
    s=input().rstrip()
    sumi=0
    for i in range(n):
        if(s[i]=='0'):
            left=i-1
            l=1
            r=1
            right=i+1
            flagl=False
            flagr=False
            while(left>=0 and flagl==False):
                if(s[left]=='1'):
                    l=i-left
                    flagl=True
                    #break
                else:
                    left-=1
            while(right<=n-1 and flagr==False):
                if(s[right]=='1'):
                    r=right-i
                    flagr=True
                    #break
                else:
                    right+=1
            if(flagl==True and flagr==True):
                sumi+=min(l,r)
            elif(flag1==True):
                sumi+=l
            else:
                sumi+=r
            
                    
                    
                    
    print('Case #'+str(te+1)+": "+str(sumi))
                    
        
