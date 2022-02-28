# python3

from typing import List, Optional
import sys
import threading
from tests.parents_test import parents
from time import process_time

class Node:
    def __init__(self, key: int) -> None:
        self.key: int = key
        self.children: Optional[List[int]] = []

class Tree:
    def __init__(self) -> None:
        self.nodes: List[Node] = {}
        
    def add_node(self, node: Node):
        self.nodes[node.key] = node

    # Optimized => O(Vertices + Edges)
    def height(self, root: Node) -> int:
        # Replace this code with a faster implementation  
        if not root.children:
            return 0

        # Recursively call height on each node
        return 1 + max(list(map(self.height, [self.nodes[x] for x in root.children])))


def compute_height(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height


def build_tree(parents) -> Tree:
    tree = Tree()
    for i, parent in enumerate(parents):
        if parent not in tree.nodes:
            parent_node = Node(key=parent)
            tree.add_node(parent_node)
        if i not in tree.nodes:
            child_node = Node(key=i)
            tree.add_node(child_node)
        tree.nodes[parent].children.append(i)
    return tree
            
def main():
    # Start the stopwatch / counter 
    t1_start = process_time() 

    #n = int(input())
    #parents = list(map(int, input().split()))
    tree = build_tree(parents)
    root = tree.nodes[-1]
    print(tree.height(root))
    

    # Stop the stopwatch / counter
    t1_stop = process_time()

    print("Elapsed time in seconds (Optimum): {}".format(t1_stop-t1_start)) 

    # -------------------------------------------------------------
    t1_start = process_time() 
    print(compute_height(len(parents), parents))
    t1_stop = process_time()
    print("Elapsed time in seconds: {}".format(t1_stop-t1_start)) 


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**28)   # new thread will get stack of such size
threading.Thread(target=main).start()