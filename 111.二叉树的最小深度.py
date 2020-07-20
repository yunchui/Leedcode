#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (42.40%)
# Likes:    292
# Dislikes: 0
# Total Accepted:    92.3K
# Total Submissions: 215K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最小深度。
# 
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回它的最小深度  2.
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
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
           
        def bfs(root):
            queue = [root]
            depth = 1
            while(queue):
                for _ in range(len(queue)):
                    #print(queue)
                    cur = queue.pop(0)
                    if cur.left:queue.append(cur.left)
                    if cur.right:queue.append(cur.right)
                    if not cur.left and not cur.right: return depth
                depth += 1
            

                
        depth = bfs(root)
        return depth
# @lc code=end

