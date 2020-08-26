#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#
# https://leetcode-cn.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (61.54%)
# Likes:    373
# Dislikes: 0
# Total Accepted:    61K
# Total Submissions: 94.3K
# Testcase Example:  '"abc"'
#
# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
# 
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
# 
# 
# 
# 示例 1：
# 
# 输入："abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
# 
# 
# 示例 2：
# 
# 输入："aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
# 
# 
# 
# 提示：
# 
# 
# 输入的字符串长度不会超过 1000 。
# 
# 
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(2*n-1):
            left = i//2
            right = left + i % 2
            while left>=0 and right<n and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans

        
        '''
        n = len(s)
        ans = 0
        dp = [[False]* n for _ in range(n)]
        for i in range(n):
            for j in range(i+1):
                if (s[i]==s[j]) and (i-j < 2 or s[i-1] == s[j+1] ):
                    dp[i][j]=True
                    ans+=1
        return ans
        '''
                
        
# @lc code=end

