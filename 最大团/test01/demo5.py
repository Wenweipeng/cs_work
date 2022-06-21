# step1:创建空图
import matplotlib.pyplot as plt
import networkx as nx
G = nx.DiGraph()  # 创建什么都没有的空图

# step2:给上述空图加边
start = [1, 3, 5, 7]  # 边的起点列表
to = [2, 4, 6, 8]  # 边的终点列表
for j in range(len(start)):
    G.add_edge(start[j], to[j])
nx.draw(G, with_labels=True)
plt.show()
# 最后两句其实不加，也没什么
