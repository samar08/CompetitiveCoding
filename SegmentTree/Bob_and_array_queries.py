'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
N = 500003
arr=[0  for i in range(N)]
tree=[0 for i in range(4*N)]
def buildtree(nl,nr,ti,arr,tree):
    if(nl==nr):
        s=str(bin(arr[nl]))[2:]
        tree[ti]=s.count('1')
        return
    m=nl+(nr-nl)//2
    buildtree(nl,m,2*ti+1,arr,tree)
    buildtree(m+1,nr,2*ti+2,arr,tree)
    tree[ti]=tree[2*ti+1]+tree[2*ti+2]
def update(nl,nr,ti,arr,tree,idx,val,typ):
    if(nl==nr):
        arr[idx]=val
        # s=str(bin(arr[idx]))[2:]
        # tree[ti]=s.count('1')
        if(typ==1):
            tree[ti]+=1
        elif(typ==2):
            if(tree[ti]!=0):
                tree[ti]-=1
        return
    m=nl+(nr-nl)//2
    if(idx<=m):
        update(nl,m,2*ti+1,arr,tree,idx,val,typ)
    else:
        update(m+1,nr,2*ti+2,arr,tree,idx,val,typ)
    tree[ti]=tree[2*ti+1]+tree[2*ti+2]
def query(nl,nr,ti,arr,tree,l,r):
    if(r<nl or l>nr):
        return 0
    if(nl>=l and nr<=r):
        return tree[ti]
    m=nl+(nr-nl)//2
    ans1=query(nl,m,2*ti+1,arr,tree,l,r)
    ans2=query(m+1,nr,2*ti+2,arr,tree,l,r)
    return ans1+ans2
n,q=list(map(int,input().split(' ')))
#arr=[0 for i in range(n)]
#tree=[0 for i in range(4*n)]
for i in range(q):
    inp=list(map(int,input().split(' ')))
    if(inp[0]==1):
        val=2*(arr[inp[1]])+1
        update(0,n-1,0,arr,tree,inp[1],val,inp[0])
    elif(inp[0]==2):
        val=arr[inp[1]]//2
        update(0,n-1,0,arr,tree,inp[1],val,inp[0])
    elif(inp[0]==3):
        print(query(0,n-1,0,arr,tree,inp[1],inp[2]))


