#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
# https://leetcode-cn.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (41.82%)
# Likes:    559
# Dislikes: 0
# Total Accepted:    103.8K
# Total Submissions: 244.2K
# Testcase Example:  '[1,2]'
#
# 请判断一个链表是否为回文链表。
# 
# 示例 1:
# 
# 输入: 1->2
# 输出: false
# 
# 示例 2:
# 
# 输入: 1->2->2->1
# 输出: true
# 
# 
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None:
            return True
        p = q = head
        pre = None
        while q:
            p = p.next
            q = q.next.next if q.next else q.next
        while p:
            p.next,p,pre = pre,p.next,p
        while head and pre:
            if head.val != pre.val:
                return False
            head = head.next
            pre = pre.next
        return True
            




# @lc code=end

