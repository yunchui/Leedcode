#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#
# https://leetcode-cn.com/problems/add-strings/description/
#
# algorithms
# Easy (49.93%)
# Likes:    174
# Dislikes: 0
# Total Accepted:    38.6K
# Total Submissions: 77.1K
# Testcase Example:  '"0"\n"0"'
#
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
# 
# 注意：
# 
# 
# num1 和num2 的长度都小于 5100.
# num1 和num2 都只包含数字 0-9.
# num1 和num2 都不包含任何前导零。
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
# 
# 
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if not num1 or not num2:
            return num1 or num2
        l1 = len(num1) - 1
        l2 = len(num2) -1 
        ans = []
        
        carry = 0
        while l1 >= 0 or l2 >= 0 or carry:
            n1 = int(num1[l1]) if l1>= 0 else 0
            n2 = int(num2[l2]) if l2 >= 0 else 0
            carry,cur = divmod(n1+n2+carry,10)
            ans.append(str(cur))
            l1,l2 = l1-1,l2-1
        return ''.join(ans[::-1])

# @lc code=end

