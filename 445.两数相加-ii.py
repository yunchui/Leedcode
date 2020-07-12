#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#
# https://leetcode-cn.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (57.29%)
# Likes:    234
# Dislikes: 0
# Total Accepted:    43.9K
# Total Submissions: 76.2K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
# 
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
# 
# 
# 
# 进阶：
# 
# 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
# 
# 
# 
# 示例：
# 
# 输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 8 -> 0 -> 7
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        stack1 = []
        stack2 = []

        while l1 or l2:
            if l1:
                stack1.append(l1.val)
                l1 = l1.next 
            if l2:
                stack2.append(l2.val)
                l2 = l2.next
        carry = 0
        head = ListNode(0)
        head.next = None

        while stack1 or stack2:
            x = stack1.pop() if stack1 else 0
            y = stack2.pop() if stack2 else 0

            s = x + y + carry
            carry = s // 10
            n = s % 10

            cur = ListNode(n)
            cur.next = head.next
            head.next = cur

        if carry != 0:
            cur = ListNode(1)
            cur.next = head.next
            head.next = cur
        return head.next








        
# @lc code=end

