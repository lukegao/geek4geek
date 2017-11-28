# -*- coding: utf-8 -*-

import itertools


def construct_segtree(inlist=None):
    if not inlist:
        return None

    tree_arr = [None] * (2*len(inlist) - 1)
    # iteratively build tree nodes
    tree_arr[-len(inlist):] = inlist

    index = len(inlist) - 1
    while(index >= 0):
        tree_arr[index] = tree_arr[2*index + 1] + tree_arr[2*index + 2]
        index -= 1

    return tree_arr


def main():
    test_list = [1, 3, 5, 7, 9, 11]
    result = construct_segtree(test_list)
    print(result)

if __name__ == '__main__':
    main()
