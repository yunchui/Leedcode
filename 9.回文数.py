#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#
# https://leetcode-cn.com/problems/palindrome-number/description/
#
# algorithms
# Easy (57.52%)
# Likes:    1196
# Dislikes: 0
# Total Accepted:    430.8K
# Total Submissions: 736.4K
# Testcase Example:  '121'
#
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# 
# 示例 1:
# 
# 输入: 121
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 
# 
# 示例 3:
# 
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
# 
# 
# 进阶:
# 
# 你能不将整数转为字符串来解决这个问题吗？
# 
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x %10 == 0 and x!=0):
            return False
        n = 0
        while n < x:
            n = x % 10 + n *10
            x = x // 10
        return n == x or x == n //10
        '''
        s = str(x)
        n = len(s)
        #print(n)
        i,j = 0,n-1
        while i != j and i<j:
            #print(i,j)
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True
        '''

# @lc code=end

