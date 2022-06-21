#Maximum Clique Problem最大团问题
#回溯法，深度优先
'''
输入：
4
1,1,1,0
1,1,1,0
1,1,1,1
0,0,1,1
'''
import copy
def Max_Clique(t):
    global bestx #最大团节点编号
    global bestn #最大团节点数
    if t >= n:
        sum = 0
        for value in x:
            sum = sum + value
        if sum > bestn:
            bestx = copy.deepcopy(x)
            bestn = sum
    else:
        #判断与当前节点是否形成团
        flag = 1
        for i in range(0,t):
            if x[i] == 1 and G_list[t][i] == '0':
                flag = 0
        if flag == 0:
            x[t] = 0
            Max_Clique(t+1)
        else:
            for j in range(0,2):
                x[t] = j
                Max_Clique(t+1)

if __name__ == '__main__':
    #输入一个图，用二维数组存储
    #输入节点数量
    print('图中节点个数为：')
    n = int(input())
    G_list = []
    print('图的邻接矩阵为：')
    for i in range(n):
        G_list.append(input().split(','))
    x = [0 for i in range(n)]
    global bestn
    bestn = 0
    Max_Clique(0)
    print('最大团节点数为：'+str(bestn))
    print('最大团中的顶点为:'+str(bestx))
