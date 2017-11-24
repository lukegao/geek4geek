# -*- coding: utf-8 -*-

from lca import Node


def left_traverse(root):
    if root is None:
        return

    left_traverse(root.left)
    print(root.key)
    left_traverse(root.right)


def mid_traverse(root):
    if root is None:
        return

    print(root.key)
    mid_traverse(root.left)
    mid_traverse(root.right)


def right_traverse(root):
    if root is None:
        return

    right_traverse(root.right)
    print(root.key)
    right_traverse(root.left)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.left = Node(8)
    root.right.left = Node(6)
    root.right.right = Node(7)
    mid_traverse(root)


if __name__ == '__main__':
    main()
