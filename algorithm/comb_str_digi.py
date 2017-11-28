# -*- coding: utf-8 -*-
"""
Combinations in a String of Digits

Given an input string of numbers, find all combinations of numbers that can be
 formed using digits in the same order.

:referrer: http://www.geeksforgeeks.org/combinations-string-digits/
"""


def resolve(instr, index, value):
    """
    Recursion func to traverse binary tree

    :param instr: Input string to be split.
    :param index: Current index in input string.
    :param value: Value stored in tree node which passed through the 
      traversing process.
    """
    if index >= len(instr):
        print(value)
        return

    cur_val = value + instr[index]

    resolve(instr, index + 1, cur_val)
    if len(instr) > index + 1:
        resolve(instr, index + 1, cur_val+',')


def main():
    s = '123456'
    resolve(s, 0, '')


if __name__ == '__main__':
    main()
