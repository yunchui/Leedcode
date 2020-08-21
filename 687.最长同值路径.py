#
# @lc app=leetcode.cn id=687 lang=python3
#
# [687] 最长同值路径
#
# https://leetcode-cn.com/problems/longest-univalue-path/description/
#
# algorithms
# Easy (40.22%)
# Likes:    308
# Dislikes: 0
# Total Accepted:    19.9K
# Total Submissions: 48.5K
# Testcase Example:  '[5,4,5,1,1,5]'
#
# 给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。
# 
# 注意：两个节点之间的路径长度由它们之间的边数表示。
# 
# 示例 1:
# 
# 输入:
# 
# 
# ⁠             5
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         1   1   5
# 
# 
# 输出:
# 
# 
# 2
# 
# 
# 示例 2:
# 
# 输入:
# 
# 
# ⁠             1
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         4   4   5
# 
# 
# 输出:
# 
# 
# 2
# 
# 
# 注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。
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
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.path = 0
        def dfs(root):
            if root == None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            leftpath = left +1 if root.left != None and root.left.val == root.val else 0
            rightpath = right +1 if root.right != None and root.right.val == root.val else 0
            self.path = max(self.path,leftpath+rightpath)
            return max(leftpath,rightpath)
        dfs(root)
        return self.path


        
# @lc code=end

