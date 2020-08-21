#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#
# https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/description/
#
# algorithms
# Easy (44.74%)
# Likes:    132
# Dislikes: 0
# Total Accepted:    17K
# Total Submissions: 37.4K
# Testcase Example:  '[1,null,2,2]'
#
# 给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
# 
# 假定 BST 有如下定义：
# 
# 
# 结点左子树中所含结点的值小于等于当前结点的值
# 结点右子树中所含结点的值大于等于当前结点的值
# 左子树和右子树都是二叉搜索树
# 
# 
# 例如：
# 给定 BST [1,null,2,2],
# 
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  2
# 
# 
# 返回[2].
# 
# 提示：如果众数超过1个，不需考虑输出顺序
# 
# 进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
class Solution:
    def __init__(self):
        self.pre = None
        self.ret = []
        self.ret_count, self.max_count, self.cur_count = 0, 0, 0

    def findMode(self, root: TreeNode) -> List[int]:
        
        self.inOrder(root)
       
        self.pre = None
        self.ret = [0] * self.ret_count
        self.ret_count, self.cur_count = 0, 0
        self.inOrder(root)
        
        return self.ret

    def inOrder(self, root: TreeNode) -> None:
        if not root:
            return
        self.inOrder(root.left)
        if self.pre and self.pre.val == root.val:
            self.cur_count += 1
        else:
            self.cur_count = 1
        if self.cur_count > self.max_count:
            self.max_count = self.cur_count
            self.ret_count = 1
        elif self.cur_count == self.max_count:
            if len(self.ret):
                self.ret[self.ret_count] = root.val
            self.ret_count += 1
        self.pre = root
        self.inOrder(root.right)



        '''
        if not root:
            return []
        ans = self.order(root)
        n = len(ans)
        target = [0,0] 
        i=0
        count =1 
        while i<n-1:
            if ans[i]==ans[i+1]:
                i +=1
                count+=1
            else:
                if count>target[0]:
                    target = [count,ans[i]]
                elif count==target[0]:
                    target.append(ans[i])    
                
                count = 1
                i += 1
         
         #最后一个
        if count>target[0]:
            target = [count,ans[i]]
        elif count==target[0]:
            target.append(ans[i])    
        return target[1:]
        
        
    def order(self,root):
        if not root:
            return []
        return self.order(root.left)+[root.val]+self.order(root.right)
        '''
            
        
# @lc code=end

