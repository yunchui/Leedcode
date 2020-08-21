#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#
# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (65.57%)
# Likes:    322
# Dislikes: 0
# Total Accepted:    138.3K
# Total Submissions: 208.8K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的 前序 遍历。
# 
# 示例:
# 
# 输入: [1,null,2,3]  
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3 
# 
# 输出: [1,2,3]
# 
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ret
# @lc code=end

