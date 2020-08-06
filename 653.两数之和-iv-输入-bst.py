#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#
# https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/description/
#
# algorithms
# Easy (55.05%)
# Likes:    162
# Dislikes: 0
# Total Accepted:    19.2K
# Total Submissions: 34.2K
# Testcase Example:  '[5,3,6,2,4,null,7]\n9'
#
# 给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
# 
# 案例 1:
# 
# 
# 输入: 
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
# 
# Target = 9
# 
# 输出: True
# 
# 
# 
# 
# 案例 2:
# 
# 
# 输入: 
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
# 
# Target = 28
# 
# 输出: False
# 
# 
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

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        nums = []
        def treeToList(root):
            if not root:
                return 
            treeToList(root.left)
            nums.append(root.val)
            treeToList(root.right)
        treeToList(root)
        i,j = 0,len(nums)-1
        while i<j:
            sum = nums[i] + nums[j]
            if sum == k:
                return True
            elif sum < k:
                i+=1
            elif sum > k:
                j -= 1
        return False
        

        

        
# @lc code=end

