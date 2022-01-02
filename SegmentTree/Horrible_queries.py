import sys
def buildtree(nl,nr,arr,tree,ti):
    if(nl==nr):
        tree[ti]=arr[nl]
        return
    m=nl+(nr-nl)//2
    buildtree(nl,m,arr,tree,(2*ti)+1)
    buildtree(m+1,nr,arr,tree,2*ti+2)
    tree[ti]=(tree[2*ti+1]+tree[2*ti+2])
def update(nl,nr,ti,arr,tree,lazy,l,r,val):
    if(lazy[ti]!=0):
        tree[ti]+=lazy[ti]*(nr-nl+1)
        if(nl!=nr):
            lazy[2*ti+1]+=lazy[ti]
            lazy[2*ti+2]+=lazy[ti]
        lazy[ti]=0
    if(l>nr or r<nl):
        return
    elif(nl>=l and nr<=r):
        tree[ti]+=(val*(nr-nl+1))
        if(nl!=nr):
            #m=nl+(nr-nl)//2
            lazy[2*ti+1]+=val
            lazy[2*ti+2]+=val
        return
    else:
        m=nl+(nr-nl)//2
        update(nl,m,2*ti+1,arr,tree,lazy,l,r,val)
        update(m+1,nr,2*ti+2,arr,tree,lazy,l,r,val)
        tree[ti]=(tree[2*ti+1]+tree[2*ti+2])
    #print(tree)

    
    
def query(nl,nr,ti,arr,tree,lazy,l,r):
    if(lazy[ti]!=0):
        tree[ti]+=lazy[ti]*(nr-nl+1)
        if(nl!=nr):
            lazy[2*ti+1]+=lazy[ti]
            lazy[2*ti+2]+=lazy[ti]
        lazy[ti]=0
    if(l>nr or r<nl):
        return 0
    elif(nl>=l and nr<=r):
        return tree[ti]
    else:
        m=nl+(nr-nl)//2
        ans1=query(nl,m,2*ti+1,arr,tree,lazy,l,r)
        ans2=query(m+1,nr,2*ti+2,arr,tree,lazy,l,r)
        return (ans1+ans2)

    


    
if __name__=='__main__':
    t=int(input())
    for te in range(t):

        #print('Enter no. of elements in array')
        n,q=list(map(int,input().split(" ")))
        arr=[0 for i in range(n)]
        #print('Enter array elements')
        #arr=list(map(int,input().split(' ')))
        tree=[]
        lazy=[]
        for i in range(4*n):
            tree.append(0)
            lazy.append(0)
        buildtree(0,n-1,arr,tree,0)
        #print(tree)
        #print('Enter no. of querys')
        #q=int(input())
        for i in range(q):
            #print('Enter query type')
            query1=list(map(int,input().split(" ")))
            if(query1[0]==0):
                #print('Enter the range l,r which you want to update')
                l,r=query1[1]-1,query1[2]-1
                #print('Enter value by which you want to update the range l and r')
                val=query1[3]
                update(0,n-1,0,arr,tree,lazy,l,r,val)
            else:
                #print('Enter l and r')
                l,r=query1[1]-1,query1[2]-1
                #print('Min element from l to r is')
                print(query(0,n-1,0,arr,tree,lazy,l,r))
