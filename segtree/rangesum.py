# -*- coding: utf-8 -*-

import itertools


def get_mid(start, end):
    return start + int((end - start)/2)


def construct_tree(inlist, ss, se, si, st):
    if not inlist:
        return None

    if ss == se:
        print(ss, si)
        st[si] = inlist[ss]
        return st[si]

    mid = get_mid(ss, se)
    st[si] = construct_tree(inlist, ss, mid, 2*si+1, st) + \
        construct_tree(inlist, mid+1, se, 2*si+2, st)

    return st[si]


def construct_segtree_iter(inlist=None):
    if not inlist:
        return None

    tree_arr = [None] * (2*len(inlist) - 1)
    # iteratively build tree nodes
    tree_arr[-len(inlist):] = inlist

    index = len(inlist) - 2
    while(index >= 0):
        tree_arr[index] = tree_arr[2*index + 1] + tree_arr[2*index + 2]
        index -= 1

    return tree_arr


def main():
    test_list = [1, 3, 5, 7, 9, 11]
    # result = construct_segtree_iter(test_list)
    result = [None] * (2*len(test_list) - 1)
    construct_tree(test_list, 0, len(test_list)-1, 0, result)
    print(result)


if __name__ == '__main__':
    main()
