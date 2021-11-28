class Solution:
    def dfs(self,start,final,graph,path,res):
        for node in graph[start]:
            path.append(node)
            if(node==final):
                new=[i for i in path]
                res.append(new)
                #print(path)
            else:
                self.dfs(node,final,graph,path,res)
            path.pop()
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        final=n-1
        res=[]
        path=[0]
        self.dfs(0,final,graph,path,res)
        return res
