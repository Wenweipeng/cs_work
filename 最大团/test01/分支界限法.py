#Maximum Clique Problem最大团问题
#分支限界法，广度优先，队列
'''
输入：
4
1,1,1,0
1,1,1,0
1,1,1,1
0,0,1,1
'''
import copy
#存储当前状态
class QueueItem:
    def __init__(self,x,w):
        self.x = x
        self.w = w

def judge_clique(t):
    # 判断与当前节点是否形成团
    flag = 1
    for j in range(0, t):
        if item.x[j] == 1 and G_list[t][j] == '0':
            flag = 0
    return flag

def EnQueue(tmp_x , tmp_w):
    global bestn
    global bestx
    tmp_item = QueueItem(tmp_x, tmp_w)
    Queuelist.insert(0,tmp_item)
    if tmp_w >= bestn:
        bestx = copy.deepcopy(tmp_x)
        bestn = tmp_w


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

    Queuelist = []  #队列
    global bestn  #当前最优最大团数量
    global bestx  # 最大团节点编号
    t = 0  #标记层数

    Queuelist.insert(0,-1)  #用于分层
    x[0] = 1
    Queuelist.insert(0, QueueItem(copy.deepcopy(x), 1))
    bestn = 1
    bestx = copy.deepcopy(x)
    x[0] = 0
    Queuelist.insert(0 , QueueItem(copy.deepcopy(x),0))

    while(True):
        item = Queuelist.pop()
        if item == -1:
            if t >= n-1 or len(Queuelist) == 0:
                print('最大团节点数为：'+str(bestn))
                print('最大团中的顶点为:'+str(bestx))
                break
            Queuelist.insert(0, -1)  # 用于分层
            item =  Queuelist.pop()
            t = t + 1
        #如果该节点可形成团，并且未来比当前最优解大，则将左孩子节点加入
        if judge_clique(t) and item.w + n - t > bestn:
            item.x[t] = 1
            EnQueue(item.x , item.w+1)
        elif item.w + n - t - 1  > bestn:
            item.x[t] = 0
            EnQueue(item.x , item.w)
