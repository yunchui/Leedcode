#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#
# https://leetcode-cn.com/problems/ones-and-zeroes/description/
#
# algorithms
# Medium (52.93%)
# Likes:    164
# Dislikes: 0
# Total Accepted:    10.2K
# Total Submissions: 19K
# Testcase Example:  '["10","0001","111001","1","0"]\n5\n3'
#
# 在计算机界中，我们总是追求用有限的资源获取最大的收益。
# 
# 现在，假设你分别支配着 m 个 0 和 n 个 1。另外，还有一个仅包含 0 和 1 字符串的数组。
# 
# 你的任务是使用给定的 m 个 0 和 n 个 1 ，找到能拼出存在于数组中的字符串的最大数量。每个 0 和 1 至多被使用一次。
# 
# 注意:
# 
# 
# 给定 0 和 1 的数量都不会超过 100。
# 给定字符串数组的长度不会超过 600。
# 
# 
# 示例 1:
# 
# 
# 输入: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
# 输出: 4
# 
# 解释: 总共 4 个字符串可以通过 5 个 0 和 3 个 1 拼出，即 "10","0001","1","0" 。
# 
# 
# 示例 2:
# 
# 
# 输入: Array = {"10", "0", "1"}, m = 1, n = 1
# 输出: 2
# 
# 解释: 你可以拼出 "10"，但之后就没有剩余数字了。更好的选择是拼出 "0" 和 "1" 。
# 
# 
#

# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len(strs) + 1)]
        for i in range(1, len(strs) + 1):
            ones = strs[i - 1].count("1")
            zeros = strs[i - 1].count("0")
            print(ones,zeros)
            for j in range(m + 1):
                for k in range(n + 1):
                    dp[i][j][k] = dp[i - 1][j][k]
                    if j >= zeros and k >= ones and dp[i][j][k] < dp[i - 1][j - zeros][k - ones] + 1:
                        dp[i][j][k] = dp[i - 1][j - zeros][k - ones] + 1
        return dp[-1][-1][-1]
        

# @lc code=end

