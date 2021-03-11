t=int(input())
for te in range(t):

    p=(input().split(" "))
    sec=0
    if(p[1]=='AM'):
        h,m=p[0].split(":")
        h=int(h)
        m=int(m)
        if(h==12):
            h=0
        sec+=h*(3600)+(m*(60))
    else:
        #sec+=12*(3600)
        h,m=p[0].split(":")
        h=int(h)
        m=int(m)
        if(h==12):
            sec=0
        else:
            sec+=12*(3600)
        sec+=h*(3600)+(m*(60))
        
        
    
    n=int(input())
    
    for i in range(n):
        start=0
        end=0
        l=input().split(" ")
        #print(l)
        if(l[1]=='AM'):
            hs,ms=l[0].split(":")
            hs=int(hs)
            ms=int(ms)
            if(hs==12):
                hs=0
            start+=hs*(3600)+(ms*(60))
        elif(l[1]=='PM'):
            
            hs,ms=l[0].split(":")
            hs=int(hs)
            ms=int(ms)
            if(hs==12):
                start=0
            else:
                start+=12*(3600)
                
            start+=hs*(3600)+(ms*(60))
        #print(start)
        if(l[3]=='AM'):
            he,me=l[2].split(":")
            he=int(he)
            me=int(me)
            if(he==12):
                he=0
            end+=he*(3600)+(me*(60))
        elif(l[3]=='PM'):
            
            he,me=l[2].split(":")
            he=int(he)
            me=int(me)
            if(he==12):
                end=0
            else:
                end+=12*(3600)
                
            end+=he*(3600)+(me*(60))
        #print(end)
        #print(sec,start,end)
        if(start<=sec and end>=sec):
            print('1',end="")
        else:
            print('0',end="")
    print(end="\n")
            
            
        
            
                
            
        #print(l)
