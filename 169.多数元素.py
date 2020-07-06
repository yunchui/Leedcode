#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
# https://leetcode-cn.com/problems/majority-element/description/
#
# algorithms
# Easy (63.28%)
# Likes:    654
# Dislikes: 0
# Total Accepted:    183K
# Total Submissions: 287.2K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
# 
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
# 
# 
# 
# 示例 1:
# 
# 输入: [3,2,3]
# 输出: 3
# 
# 示例 2:
# 
# 输入: [2,2,1,1,1,2,2]
# 输出: 2
# 
# 
#

# @lc code=start
#Boyer-Moore Majority Vote Algorithm解法
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        maj = nums[0]
        for num in nums:
            if cnt == 0:
                maj = num 
            cnt = cnt+1 if maj == num else cnt - 1
        return maj
# @lc code=end

