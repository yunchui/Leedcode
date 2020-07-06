#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#
# https://leetcode-cn.com/problems/maximum-product-of-three-numbers/description/
#
# algorithms
# Easy (50.01%)
# Likes:    141
# Dislikes: 0
# Total Accepted:    21.4K
# Total Submissions: 42.5K
# Testcase Example:  '[1,2,3]'
#
# 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
# 
# 示例 1:
# 
# 
# 输入: [1,2,3]
# 输出: 6
# 
# 
# 示例 2:
# 
# 
# 输入: [1,2,3,4]
# 输出: 24
# 
# 
# 注意:
# 
# 
# 给定的整型数组长度范围是[3,10^4]，数组中所有的元素范围是[-1000, 1000]。
# 输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。
# 
# 
#

# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        '''
        if nums[0]*nums[1]*nums[2] <= 0:
            if nums[0] >= 0:
                return 0
            else:
                return nums[0] * nums[len(nums)-1]*nums[len(nums)-2]
            '''

        return max(nums[0]*nums[1]*nums[2],nums[0] * nums[len(nums)-1]*nums[len(nums)-2])
        
# @lc code=end

