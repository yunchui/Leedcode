#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
# https://leetcode-cn.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (49.01%)
# Likes:    505
# Dislikes: 0
# Total Accepted:    74.3K
# Total Submissions: 143.4K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# 给定一个未排序的整数数组，找出最长连续序列的长度。
# 
# 要求算法的时间复杂度为 O(n)。
# 
# 示例:
# 
# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
# 
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums_set = set(nums)
        for num in nums_set:
            num_current = num
            res_current = 1
            while num_current +1 in nums_set:
                num_current += 1
                res_current += 1
            res = max(res,res_current)
        return res
# @lc code=end

