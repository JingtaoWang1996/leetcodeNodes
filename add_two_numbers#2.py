"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and
return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself
"""
"""
可能的方法
注意：1）倒叙链表 2）前置0 3）链表非空 4）链表形式正确返回求和的值
1、暴力：直接便利两个链表得到值后，求和以链表形式返回
2、链表操作: 两个链表求和到其中一个链表当中+链表转置
   pS: 无法直接跑，因为定义了链表class
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseLinkList(self, rev_l):
        # only 1 node
        if rev_l.next is None:
            return rev_l
        # node nums >=2
        p1 = rev_l.next
        while p1 is not None:
            p2 = p1.next
            p1.next = rev_l
            rev_l.next = None
            rev_l = p1
            p1 = p2
        return rev_l

    def addSingleLinkList(self, single_l, add):
        while single_l is not None:
            res = single_l.val + add
            single_l.val = res % 10
            add = res // 10
            single_l = single_l.next
        if add == 1:
            node = ListNode()
            node.next = None
            node.val = 1
            single_l.next = node # None

    def addTwoNumbers(self, l1, l2):
        # check both linkList are nonEmpty
        if l1 is None:
            return self.reverseLinkList(l2)
        if l2 is None:
            return self.reverseLinkList(l1)
        # both non-empty，add l1 to l2
        add = 0
        head = l2
        while l1 is not None and l2 is not None:
            res = l1.val + l2.val + add
            l2.val = res % 10
            add = res // 10
            if l1.next is None or l2.next is None:
                break
            l1 = l1.next
            l2 = l2.next
        if l1 is None:  # l1 shorter than l2
            self.addSingleLinkList(l2, add)
        else:
            l2.next = l1.next
            self.addSingleLinkList(l1, add)
        return head


if __name__ == '__main__':
    solution = Solution()
