# -*- coding: utf-8 -*-


class Node(object):

    # Constructor to create a new tree node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
