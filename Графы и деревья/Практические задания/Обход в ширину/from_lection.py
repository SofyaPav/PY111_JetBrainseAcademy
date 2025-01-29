import networkx as nx  # pip install networkx
import matplotlib.pyplot as plt  # pip3 install matplotlib

'''
graph = nx.Graph()  # не направленный не мультиграф
graph.add_edges_from([  # инициализация графа через список ребер
    (1, 2),
    (1, 1),  # петля
])
a = nx.draw_networkx(graph)
plt.savefig('gr.png')
plt.show()
'''

'''
graph = nx.Graph()  # не направленный не мультиграф
graph.add_edges_from([
    (1, 2),
    (1, 3),
    (2, 4),
    (2, 3),
    (3, 2),
    (4, 3),
])
nx.draw_networkx(graph)
plt.show()
'''

'''
graph = nx.Graph()  # не направленный не мультиграф
graph.add_edges_from([
    (1, 2),
    (2, 3),
    (2, 4),
])
nx.draw_networkx(graph)
plt.show()
'''

graph = nx.Graph()
graph.add_nodes_from("ABCDEFGHIJ")
graph.add_edges_from([
        ('A', 'B'),
        ('A', 'F'),
        ('B', 'G'),
        ('F', 'G'),
        ('G', 'C'),
        ('G', 'H'),
        ('G', 'I'),
        ('C', 'H'),
        ('I', 'H'),
        ('H', 'D'),
        ('H', 'E'),
        ('H', 'J'),
        ('E', 'D'),
    ])

nx.draw_networkx(graph)
plt.show()