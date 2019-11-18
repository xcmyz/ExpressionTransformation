import networkx as nx
import matplotlib.pyplot as plt
import os


def create_graph(G, node, pos={}, x=0, y=0, layer=1):
    pos.update({node.val: (x, y)})
    if node.left:
        G.add_edge(node.val, node.left.val)
        l_x, l_y = x - 10 / 2 ** layer, y - 1
        l_layer = layer + 1
        create_graph(G, node.left, x=l_x, y=l_y, pos=pos, layer=l_layer)
    if node.right:
        G.add_edge(node.val, node.right.val)
        r_x, r_y = x + 10 / 2 ** layer, y - 1
        r_layer = layer + 1
        create_graph(G, node.right, x=r_x, y=r_y, pos=pos, layer=r_layer)
    return (G, pos)


def draw(node):
    graph = nx.DiGraph()
    graph, pos = create_graph(graph, node)
    _, ax = plt.subplots(figsize=(80, 30))
    nx.draw_networkx(graph, pos, ax=ax, node_size=1000)
    if not os.path.exists("img"):
        os.mkdir("img")
    plt.savefig("img/test.jpg")
