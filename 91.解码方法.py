#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#
# https://leetcode-cn.com/problems/decode-ways/description/
#
# algorithms
# Medium (23.55%)
# Likes:    396
# Dislikes: 0
# Total Accepted:    50.6K
# Total Submissions: 213.3K
# Testcase Example:  '"12"'
#
# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。
# 
# 示例 1:
# 
# 输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
# 
# 
# 示例 2:
# 
# 输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
# 
# 
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        n = len(s)
        dp = [0]*n
        dp[0] = 1
        
        for i in range(1,n):
            if s[i] != '0':
                dp[i] = dp[i-1]
                
            num = 10*(ord(s[i-1])- ord('0')) + (ord(s[i])-ord('0'))
            
            if 10<= num <= 26:
                if i == 1:
                    dp[i] = dp[i]+1
                    #print(dp)
                else:
                    dp[i] += dp[i-2]
            
            #print(dp)
        return dp[-1]
                


# @lc code=end

