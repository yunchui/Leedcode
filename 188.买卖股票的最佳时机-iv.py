#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/description/
#
# algorithms
# Hard (29.56%)
# Likes:    237
# Dislikes: 0
# Total Accepted:    22.1K
# Total Submissions: 74.2K
# Testcase Example:  '2\n[2,4,1]'
#
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
# 
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 
# 示例 1:
# 
# 输入: [2,4,1], k = 2
# 输出: 2
# 解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
# 
# 
# 示例 2:
# 
# 输入: [3,2,6,5,0,3], k = 2
# 输出: 7
# 解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4
# 。
# 随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
# 
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [[[0,0]for _ in range(k+1)]for _ in range(n)]
        def maxProfit_l(prices):
            dp_i_0,dp_i_1 = 0,-prices[0]
            for price in prices:
                dp_i_0 = max(dp_i_0,dp_i_1+price)
                dp_i_1 = max(dp_i_1,dp_i_0-price)
            return dp_i_0
        if k > n/2:
            return maxProfit_l(prices)
        for i in range(n):
            for j in range(k):
                if i-1 == -1:
                    dp[i][j][1] = 0
                    dp[i][j][0] = 0
                dp[i][j][1] = max(dp[i][j][0]-prices[i],dp[i][j][1])
                dp[i][j][0] = max(dp[i][j][0],dp[i][j][1]+prices[i])
        return dp[-1][k][0]
             
# @lc code=end

