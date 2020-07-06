#
# @lc app=leetcode.cn id=462 lang=python3
#
# [462] 最少移动次数使数组元素相等 II
#
# https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements-ii/description/
#
# algorithms
# Medium (58.07%)
# Likes:    81
# Dislikes: 0
# Total Accepted:    6.2K
# Total Submissions: 10.7K
# Testcase Example:  '[1,2,3]'
#
# 给定一个非空整数数组，找到使所有数组元素相等所需的最小移动数，其中每次移动可将选定的一个元素加1或减1。 您可以假设数组的长度最多为10000。
# 
# 例如:
# 
# 
# 输入:
# [1,2,3]
# 
# 输出:
# 2
# 
# 说明：
# 只有两个动作是必要的（记得每一步仅可使其中一个元素加1或减1）： 
# 
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
# 
# 
#

# @lc code=start
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        l = len(nums)
        mid = l // 2
        i,j = 0,l-1
        count = 0
        while i < mid or j > mid:
            count += abs(nums[mid] - nums[i]) if i < mid else 0
            count += abs(nums[j] - nums[mid]) if j > mid else 0
            i,j = i+1,j-1
        return count







        
# @lc code=end

