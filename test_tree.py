from tree import Tree
from node import Node

def test_tree_find_1():
    node = Node(7)
    assert Tree()._find(7, node) == node

def test_tree_find_2():
    assert Tree()._find(6, Node(7)) is None