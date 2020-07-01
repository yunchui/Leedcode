#
# @lc app=leetcode.cn id=417 lang=python3
#
# [417] 太平洋大西洋水流问题
#
# https://leetcode-cn.com/problems/pacific-atlantic-water-flow/description/
#
# algorithms
# Medium (41.76%)
# Likes:    103
# Dislikes: 0
# Total Accepted:    8.1K
# Total Submissions: 19.3K
# Testcase Example:  '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
#
# 给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。“太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。
# 
# 规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。
# 
# 请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。
# 
# 
# 
# 提示：
# 
# 
# 输出坐标的顺序不重要
# m 和 n 都小于150
# 
# 
# 
# 
# 示例：
# 
# 
# 
# 
# 给定下面的 5x5 矩阵:
# 
# ⁠ 太平洋 ~   ~   ~   ~   ~ 
# ⁠      ~  1   2   2   3  (5) *
# ⁠      ~  3   2   3  (4) (4) *
# ⁠      ~  2   4  (5)  3   1  *
# ⁠      ~ (6) (7)  1   4   5  *
# ⁠      ~ (5)  1   1   2   4  *
# ⁠         *   *   *   *   * 大西洋
# 
# 返回:
# 
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (上图中带括号的单元).
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        res1 = set()
        res2 = set()
        raw = len(matrix)
        col = len(matrix[0])
        def dfs(x,y,res):
            res.add((x,y))
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                next_x,next_y = x+dx,y+dy
                if 0<=next_x<raw and 0<=next_y<col and matrix[x][y]<=matrix[next_x][next_y] and (next_x,next_y) not in res:
                    dfs(next_x,next_y,res)
        
        for i in range(raw):
            dfs(i,0,res1)
            dfs(i,col-1,res2)
        for j in range(col):
            dfs(0,j,res1)
            dfs(raw-1,j,res2)
        return res1 & res2


        
# @lc code=end

