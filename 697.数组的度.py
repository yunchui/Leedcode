#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#
# https://leetcode-cn.com/problems/degree-of-an-array/description/
#
# algorithms
# Easy (54.57%)
# Likes:    169
# Dislikes: 0
# Total Accepted:    23.2K
# Total Submissions: 42.6K
# Testcase Example:  '[1,2,2,3,1]'
#
# 给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。
# 
# 你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
# 
# 示例 1:
# 
# 
# 输入: [1, 2, 2, 3, 1]
# 输出: 2
# 解释: 
# 输入数组的度是2，因为元素1和2的出现频数最大，均为2.
# 连续子数组里面拥有相同度的有如下所示:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# 最短连续子数组[2, 2]的长度为2，所以返回2.
# 
# 
# 示例 2:
# 
# 
# 输入: [1,2,2,3,1,4,2]
# 输出: 6
# 
# 
# 注意:
# 
# 
# nums.length 在1到50,000区间范围内。
# nums[i] 是一个在0到49,999范围内的整数。
# 
# 
#

# @lc code=start
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        #1.先找到度，用字典统计，再找最大统计数，即为度
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 0
            dic[i] += 1
                
        du = max(dic.values())
        if du == 1:
            return 1
         
        #根据度找数，找出所有最大度的数
        num = []
        for i in dic:
            if dic[i] == du:
                num.append(i)
        
        #根据数找该数最大最小下标，根据下标计算最短连续子数组
        start, end = 0, 0
        num_length = []
        for i in num:
            #设置flag,记录最小下标（第一次出现的下标）
            flag = 1
            for j in range(len(nums)):
                #不断更新最大下标
                if nums[j] == i:
                    end = j
                #记录第一次的下标
                if flag == 1:
                    if nums[j] == i:
                        start = j
                        flag -= 1
            num_length.append(end-start+1)
        return min(num_length)
# @lc code=end

