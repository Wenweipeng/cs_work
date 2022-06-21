import networkx as nx
import matplotlib.pyplot as plt
# 创建空的网格
G = nx.Graph()
# 添加节点
G.add_node('JFK')
G.add_nodes_from(['SFO', 'LAX', 'ATL', 'FLO', 'DFW', 'HNL'])
# G.number_of_nodes()  # 查看节点数，输出结果7

# 添加连线
G.add_edges_from([('JFK', 'SFO'), ('JFK', 'LAX'), ('LAX', 'ATL'),
                 ('FLO', 'ATL'), ('ATL', 'JFK'), ('FLO', 'JFK'), ('DFW', 'HNL')])
G.add_edges_from([('OKC', 'DFW'), ('OGG', 'DFW'), ('OGG', 'LAX')])
# 绘制网络图
# nx.draw(G,pos=nx.circular_layout(G),with_labels=True)
nx.draw_networkx(G, pos=nx.circular_layout(G), with_labels=True, alpha=0.5, node_color='yellow', node_shape='s',
                 linewidths=4,
                 width=2, edge_color='blue', style='--',
                 font_size=15, font_color='blue', font_family='SimHei')

# pos选用圆形样式，with_labels=True在节点上绘制标签，alpha=0.5节点透明度
# linewidths=4节点边框宽度为4，node_color='yellow'节点颜色设为黄色，node_shape='s'节点的形状设为正方形
# width=2边的线宽2,edge_color='blue'设置边的颜色,style='--'边的线样式，
# font_size=15设置标签字号大小,font_color='blue'设置标签字体颜色,font_family='SimHei'设置标签字体
plt.show()
