#
# @lc app=leetcode.cn id=677 lang=python3
#
# [677] 键值映射
#
# https://leetcode-cn.com/problems/map-sum-pairs/description/
#
# algorithms
# Medium (60.99%)
# Likes:    49
# Dislikes: 0
# Total Accepted:    8K
# Total Submissions: 13.2K
# Testcase Example:  '["MapSum", "insert", "sum", "insert", "sum"]\n' +
  '[[], ["apple",3], ["ap"], ["app",2], ["ap"]]'
#
# 实现一个 MapSum 类里的两个方法，insert 和 sum。
# 
# 对于方法 insert，你将得到一对（字符串，整数）的键值对。字符串表示键，整数表示值。如果键已经存在，那么原来的键值对将被替代成新的键值对。
# 
# 对于方法 sum，你将得到一个表示前缀的字符串，你需要返回所有以该前缀开头的键的值的总和。
# 
# 示例 1:
# 
# 输入: insert("apple", 3), 输出: Null
# 输入: sum("ap"), 输出: 3
# 输入: insert("app", 2), 输出: Null
# 输入: sum("ap"), 输出: 5
# 
# 
#

# @lc code=start
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic={}
        

    def insert(self, key: str, val: int) -> None:
        self.dic[key]=val

    def sum(self, prefix: str) -> int:
        rs=0
        for key in self.dic:
            if key[0:prefix.__len__()]==prefix:
                rs=rs+self.dic[key]
        return rs
# @lc code=end

