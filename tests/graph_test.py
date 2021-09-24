import pytest 
from graphs_trees.graph import Graph, graph_from_adjacency


@pytest.fixture
def my_graph():
    M1 = [[0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 1, 1],
    [0, 1, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 1, 0]]
    G = graph_from_adjacency(M1)
    return G

def test_bfs(my_graph):
    assert my_graph.bfs(0) == [0, 2, 3, 5, 7, 6, 1, 4]


def test_dfs(my_graph):
    assert my_graph.dfs(0) == [0, 2, 5, 3, 7, 6, 1, 4]
