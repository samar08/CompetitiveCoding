t=int(input())
for te in range(t):
    n=int(input())
    a=list(map(int,input().split(" ")))
    a.sort()
    low=a[0]
    high=a[n-1]
    if(n%2==0):
        mid1=a[n//2]
        mid2=a[(n//2)-1]
        val1=abs(high-low)+abs(mid1-low)+abs(high-mid1)
        val2=abs(high-low)+abs(mid2-low)+abs(high-mid2)
        print(max(val1,val2))
    else:
        mid=a[n//2]
        val=abs(high-low)+abs(mid-low)+abs(high-mid)
        print(val)
    
