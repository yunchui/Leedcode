#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (38.60%)
# Likes:    879
# Dislikes: 0
# Total Accepted:    193.9K
# Total Submissions: 497.8K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
# 
# 示例：
# 
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
# 
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 
# 
# 说明：
# 
# 给定的 n 保证是有效的。
# 
# 进阶：
# 
# 你能尝试使用一趟扫描实现吗？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        global i
        if head == None:
            i = 0
            return None
        head.next = self.removeNthFromEnd(head.next,n)
        i += 1
        return head.next if i == n else head

'''
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None:
            return head
        head_N = ListNode(None)
        head_N.next = head
        p = q = head_N
        i = 0
        while q.next != None:
            if i < n:
                q = q.next
                i+=1
            else:
                p = p.next
                q = q.next
        if p.next == head:
            head = head.next
        else:
            p.next = p.next.next
    
        return head

         
'''




# @lc code=end

