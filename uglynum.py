# -*- coding: utf-8 -*-


def compute_ugly_nth(nth):

    tar_arr = []
    tar_arr.append(1)

    index_arr2 = 0
    index_arr3 = 0
    index_arr5 = 0

    next_i2 = 2
    next_i3 = 3
    next_i5 = 5

    for i in range(1, nth):
        value = min(
            next_i2,
            next_i3,
            next_i5
        )

        tar_arr.append(value)

        if value == next_i2:
            index_arr2 += 1
            next_i2 = tar_arr[index_arr2] * 2

        if value == next_i3:
            index_arr3 += 1
            next_i3 = tar_arr[index_arr3] * 3

        if value == next_i5:
            index_arr5 += 1
            next_i5 = tar_arr[index_arr5] * 5

    return tar_arr


def main():
    print('result:', compute_ugly_nth(15))

if __name__ == '__main__':
    main()