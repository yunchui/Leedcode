#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#
# https://leetcode-cn.com/problems/find-bottom-left-tree-value/description/
#
# algorithms
# Medium (69.97%)
# Likes:    100
# Dislikes: 0
# Total Accepted:    17.6K
# Total Submissions: 24.9K
# Testcase Example:  '[2,1,3]'
#
# 给定一个二叉树，在树的最后一行找到最左边的值。
# 
# 示例 1:
# 
# 
# 输入:
# 
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 
# 输出:
# 1
# 
# 
# 
# 
# 示例 2: 
# 
# 
# 输入:
# 
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   5   6
# ⁠      /
# ⁠     7
# 
# 输出:
# 7
# 
# 
# 
# 
# 注意: 您可以假设树（即给定的根节点）不为 NULL。
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
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [root]
        while(queue):
            root = queue.pop(0)
            if root.right: queue.append(root.right)
            if root.left: queue.append(root.left)
        return root.val

        
# @lc code=end

