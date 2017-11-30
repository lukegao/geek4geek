# -*- coding: utf-8 -*-
"""
Construction of Segment Tree from given array

Basically, building a segment tree is divide and conquer.

We start with a segment arr[0 . . . n-1].
and every time we divide the current segment into two halves
(if it has not yet become a segment of length 1),
and then call the same procedure on both halves,
and for each such segment, we store the minimum value in a segment tree node.

All levels of the constructed segment tree will be completely filled
except the last level. Also, the tree will be a Full Binary Tree because
we always divide segments in two halves at every level.
Since the constructed tree is always full binary tree with n leaves,
there will be n-1 internal nodes. So total number of nodes will be 2*n – 1.
Height of the segment tree will be upper-bound of 2*logn,
Since the tree is represented using array and relation between parent and child
indexes must be maintained, size of memory allocated for segment tree will be
 2*pow(2, logn) - 1.
"""

import math
from rangesum import get_mid


def find_rmq(iarr, qs, qe, oarray, ss, se, index):
    if not iarr:
        return math.inf

    if qs == qe:
        return iarr[qs]

    print(ss, se, index)
    mid = get_mid(ss, se)
    if qs <= ss and se <= qe:
        return oarray[index]
    elif qs > se or qe < ss:
        return math.inf
    else:
        return min(
            find_rmq(iarr, qs, qe, oarray, ss, mid, 2*index + 1),
            find_rmq(iarr, qs, qe, oarray, mid+1, se, 2*index + 2)
            )


def construct_segtree(iarr, start, end, oarray, index):
    if iarr is None:
        return

    if end == start:
        oarray[index] = iarr[start]
        return oarray[index]

    mid = get_mid(start, end)
    oarray[index] = min(construct_segtree(iarr, start, mid, oarray, 2*index + 1),
                        construct_segtree(iarr, mid+1, end, oarray, 2*index + 2))
    return oarray[index]


def main():
    test = [2, 5, 1, 4, 9, 3]
    height = math.ceil(math.log2(len(test)))
    print('Tree height:', height)

    out_array = [None] * (2 * pow(2, height) - 1)
    construct_segtree(test, 0, len(test)-1, out_array, 0)
    print('Out array:', out_array)

    value = find_rmq(test, 3, 5, out_array, 0, len(test) - 1, 0)
    print('range minium value:', value)

if __name__ == '__main__':
    main()
