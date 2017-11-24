# -*- coding: utf-8 -*-
"""
Combinations in a String of Digits

Given an input string of numbers, find all combinations of numbers that can be
 formed using digits in the same order.

:referrer: http://www.geeksforgeeks.org/combinations-string-digits/
"""


def resolve(instr, index, value):
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
