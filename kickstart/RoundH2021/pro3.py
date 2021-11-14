t=int(input())
for te in range(t):
    n=int(input())
    s=input().rstrip()
    d={}
    d['01']='2'
    d['12']='3'
    d['23']='4'
    d['34']='5'
    d['45']='6'
    d['56']='7'
    d['67']='8'
    d['78']='9'
    d['89']='0'
    d['90']='1'
    ops=['01','12','23','34','45','56','67','78','89','90']
    nops=len(ops)
    old=s
    #print(old)
    for i in range(nops):
        
        #ind=[]
        s=s.replace(ops[i],d[ops[i]])
        #print('s:',s)
        
        '''
        for j in range(len(s)-1):
            if(s[j:j+2]==ops[i]):
                ind.append(j)
        for k in range(len(ind)):
            st=s[ind[k]:ind[k]+2]
        '''
    new=s
    #print(new)
    while(old!=new):
        #old="".join(list(new))
        old=new
        for i in range(nops):
            #ind=[]
            new=new.replace(ops[i],d[ops[i]])
        
        
        
            
        
                
                
        


    print('Case #'+str(te+1)+": "+str(new))
