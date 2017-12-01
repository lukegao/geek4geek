# -*- coding: utf-8 -*-


class LinkNode:

    def __init__(self, data):
        self.data = data
        self.next = None


def build_link_list(inarr=None):
    pre = cur = None
    head = LinkNode(inarr[0])
    cur = head

    for _, item in enumerate(inarr[1:]):
        cur.next = LinkNode(item)
        cur = cur.next
    return head


def print_link_list(head=None):

    cur = head
    while cur:
        if cur.next:
            print(cur.data, end=' -> ')
        else:
            print(cur.data, ' -> Null')
        cur = cur.next
    print()


def reverse(head):
    cur = head
    pre = None

    while cur and cur.next:
        post = cur.next
        cur.next = pre
        pre = cur
        cur = post

    cur.next = pre
    head = cur
    return head


def main():
    test = list(range(0, 10))

    h = build_link_list(test)
    print_link_list(h)

    rh = reverse(h)
    print_link_list(rh)

if __name__ == '__main__':
    main()
