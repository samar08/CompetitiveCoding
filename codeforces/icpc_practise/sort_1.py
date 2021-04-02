f=open("sort_input.txt","r")
f1=f.readlines()
c=0
a=[]
for line in f1:
    if(c==0):
        x=list(map(int,line.split(" ")))
        n=x[0]
        c+=1
    else:
        x=list(map(int,line.split(" ")))
        for i in x:
            a.append(i)
a.sort()
out_f=open("sort_output.txt","w+")
for i in a:
    out_f.write('%d ' % i)
f.close()
    
