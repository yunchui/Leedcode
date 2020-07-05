#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
# https://leetcode-cn.com/problems/add-binary/description/
#
# algorithms
# Easy (52.68%)
# Likes:    425
# Dislikes: 0
# Total Accepted:    111.1K
# Total Submissions: 204.8K
# Testcase Example:  '"11"\n"1"'
#
# 给你两个二进制字符串，返回它们的和（用二进制表示）。
# 
# 输入为 非空 字符串且只包含数字 1 和 0。
# 
# 
# 
# 示例 1:
# 
# 输入: a = "11", b = "1"
# 输出: "100"
# 
# 示例 2:
# 
# 输入: a = "1010", b = "1011"
# 输出: "10101"
# 
# 
# 
# 提示：
# 
# 
# 每个字符串仅由字符 '0' 或 '1' 组成。
# 1 <= a.length, b.length <= 10^4
# 字符串如果不是 "0" ，就都不含前导零。
# 
# 
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a or not b:
            return a or b
        n1,n2 = len(a),len(b)
        print(n1,n2)
        a,b,ans = a[::-1],b[::-1],[]
        i = j = carry = 0
        while i < n1 or j < n2 or carry:
            print(carry)
            a1 = int(a[i]) if i<n1 else 0
            a2 = int(b[i]) if j<n2 else 0
            carry,cur = divmod(a1+a2+carry,2)
            ans.append(str(cur))
            i,j = i+1,j+1
        return ''.join(ans[::-1])


        
# @lc code=end

