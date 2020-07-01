#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
# https://leetcode-cn.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (47.26%)
# Likes:    301
# Dislikes: 0
# Total Accepted:    35.2K
# Total Submissions: 73.7K
# Testcase Example:  '[1,5,11,5]'
#
# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
# 
# 注意:
# 
# 
# 每个数组中的元素不会超过 100
# 数组的大小不会超过 200
# 
# 
# 示例 1:
# 
# 输入: [1, 5, 11, 5]
# 
# 输出: true
# 
# 解释: 数组可以分割成 [1, 5, 5] 和 [11].
# 
# 
# 
# 
# 示例 2:
# 
# 输入: [1, 2, 3, 5]
# 
# 输出: false
# 
# 解释: 数组不能分割成两个元素和相等的子集.
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums%2 != 0:
            return False
        h = sum_nums//2 
        nums.sort()
        pre = [False]*(h+1)
        cur = [False]*(h+1)
        pre[0] = True
        if nums[0]<=(h+1):
            pre[nums[0]] = True

        for i in range(1,len(nums)):
            for j in  range(h+1):
                if j >= nums[i]:
                    cur[j] = pre[j] or pre[j-nums[i]]
                else:
                    cur[j]= pre[j]
            pre = cur
            cur = [False]*(h+1)

        return pre[-1]

        
# @lc code=end

