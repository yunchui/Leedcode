#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#
# https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/description/
#
# algorithms
# Easy (64.49%)
# Likes:    137
# Dislikes: 0
# Total Accepted:    22.6K
# Total Submissions: 34.8K
# Testcase Example:  '[3,9,20,15,7]'
#
# 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。
# 
# 
# 
# 示例 1：
# 
# 输入：
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 输出：[3, 14.5, 11]
# 解释：
# 第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
# 
# 
# 
# 
# 提示：
# 
# 
# 节点值的范围在32位有符号整数范围内。
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []

        res = []
        queue = [root]
        
        while queue:
            cur = []  # 保存当前层的遍历值，因为queue保存的是TreeNode类型
            nxt = []  # 保存下一层的节点
            for node in queue:
                cur.append(node.val)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
 
            '''记录平均值'''
            res.append(sum(cur)/len(cur))  
            queue = nxt  # 每次更新queue
        
        return res

# @lc code=end

