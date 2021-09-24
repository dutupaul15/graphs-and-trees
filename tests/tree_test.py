import pytest
from graphs_trees.tree import Node


@pytest.fixture
def my_tree():
    n1 = Node(value=2)
    n2 = Node(value=7)
    n3 = Node(value=5)
    n4 = Node(value=10)
    n5 = Node(value=6)
    n6 = Node(value=9)
    n7 = Node(value=5)
    n8 = Node(value=11)
    n9 = Node(value=4)

    n1.add_left(n2)
    n1.add_right(n3)
    n2.add_left(n4)
    n2.add_right(n5)
    n3.add_right(n6)
    n5.add_left(n7)
    n5.add_right(n8)
    n6.add_right(n9)

    return n1


def test_postorder(my_tree):
    res = []
    assert my_tree.postorder(res) == [10, 5, 11, 6, 7, 4, 9, 5, 2]
