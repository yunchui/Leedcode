#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#
# https://leetcode-cn.com/problems/base-7/description/
#
# algorithms
# Easy (49.01%)
# Likes:    48
# Dislikes: 0
# Total Accepted:    13.3K
# Total Submissions: 27K
# Testcase Example:  '100'
#
# 给定一个整数，将其转化为7进制，并以字符串形式输出。
# 
# 示例 1:
# 
# 
# 输入: 100
# 输出: "202"
# 
# 
# 示例 2:
# 
# 
# 输入: -7
# 输出: "-10"
# 
# 
# 注意: 输入范围是 [-1e7, 1e7] 。
# 
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        n = abs(num)
        st = ""
        while n != 0:
            st = str(n%7) + st
            n = n // 7
        if num < 0:
            st = '-'+st
        return st 
# @lc code=end

