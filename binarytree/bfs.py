# -*- coding: utf-8 -*-
"""Breadth First Trasversal binary tree"""


class Node:

    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def bfs_tree(root=None):

    if not root:
        return

    queue = []
    queue.append(root)

    while (len(queue) > 0):
        cur_node = queue.pop(0)
        print(cur_node.key)

        if cur_node.left:
            queue.append(cur_node.left)
        if cur_node.right:
            queue.append(cur_node.right)


def main():
    root = Node(0)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)

    bfs_tree(root)


if __name__ == '__main__':
    main()