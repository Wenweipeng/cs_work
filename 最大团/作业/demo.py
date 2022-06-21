import networkx as nx
import matplotlib.pyplot as plt

# nodes = [
#     '1',
#     '2',
#     '3',
#     '4',
#     '5',
#     '6',
#     '7',
#     '8',
#     '9',
#     '10',
#     '11',
#     '12',
#     '13',
# ]

# edges = [
#     ('1', '3'),
#     ('2', '5'),
#     ('3', '11'),
#     ('4', '2'),
#     ('5', '13'),
#     ('6', '7'),
#     ('7', '8'),
#     ('8', '4'),
#     ('9', '12'),
#     ('10', '9'),
#     ('11', '6'),
#     ('13', '10')
# ]

# G = nx.Graph()

# for node in nodes:
#     G.add_node(node)

# G.add_edges_from(edges)

# nx.draw(G, with_labels=True, node_color="y")

# plt.show()

def visual(edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    nx.draw(G, with_labels=True, node_color="y")
    plt.show()

if __name__=='__main__':
    n=int(input('请输入节点数：'))
    e=int(input('请输入边数：'))
    edges=[]
    for edge in range(e):
        print('请输入边起始和终止的两个节点（以空格分隔）：')
        node1,node2=input().split()
        edges.append((node1,node2))
    print(edges)
    visual(edges)
