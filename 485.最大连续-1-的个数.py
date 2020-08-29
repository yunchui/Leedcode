#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续1的个数
#
# https://leetcode-cn.com/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (56.48%)
# Likes:    116
# Dislikes: 0
# Total Accepted:    50.4K
# Total Submissions: 88.8K
# Testcase Example:  '[1,0,1,1,0,1]'
#
# 给定一个二进制数组， 计算其中最大连续1的个数。
# 
# 示例 1:
# 
# 
# 输入: [1,1,0,1,1,1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
# 
# 
# 注意：
# 
# 
# 输入的数组只包含 0 和1。
# 输入数组的长度是正整数，且不超过 10,000。
# 
# 
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        #dic = {}
        count = 0
        countMax = 0

        for num in nums:
            if num== 0:
                countMax = max(countMax,count)
                count = 0
            else:
                count+=1
        countMax = max(countMax,count)
        return countMax
                

            
        
# @lc code=end

