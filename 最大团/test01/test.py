global v,e,graph#v为顶点数，e为边数，graph为邻接矩阵
global cn,bestn#cn当前团的顶点数，bestn最大团的顶点数
global corder,bestorder#corder当前团的顶点集，bestorder最大团的顶点集
global vis#记录已选的顶点
vis=[0 for i in range(100)]
corder=[0 for i in range(100)]
bestorder=[0 for i in range(100)]
def istuan(cur):
    global vis,graph
    for i in range(cur):
        if((vis[i]==1) and(graph[i][cur]==0)):
            return 0
    return 1
 
def backtrack(cur):
    global v,bestn,corder,cn,vis#python中定义全局变量，先定义，使用时再次声明
    # if (cur>v-1):
    if(cur>v):
        if (cn>bestn):
            bestn=cn
            for i in range(v+1):
                if corder[i]!=0:
                    print(corder[i],'',end='')
        print()
        return
    if(istuan(cur)):
        cn+=1
        vis[cur]=1
        corder[cur]=cur
        backtrack(cur+1)
        cn-=1
        vis[cur]=0
        corder[cur]=0
    #回溯到i，为进入右子树做准备
    if ((cn+v-cur)>bestn):#剪右枝条件，否则向右递归
        backtrack(cur+1)
if __name__=='__main__':
    # global graph,cn,bestn
    cn=0
    bestn=0
    v=5;e=7
    # graph=[[0,1,0,1,1],[1,0,1,0,1],[0,1,0,0,1],[1,0,0,0,1],[1,1,1,1,0]]
    graph=[[0 for i in range(v+1)] for j in range(v+1)]
    print(graph)
    for k in range(1,e+1):
        i,j=map(int,input().split())
        graph[i][j]=1
    print(graph)
    backtrack(1)
    print(bestn)
 