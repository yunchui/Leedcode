#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
# https://leetcode-cn.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (39.93%)
# Likes:    215
# Dislikes: 0
# Total Accepted:    35.4K
# Total Submissions: 88.7K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
# 
# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
# 
# 示例:
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# 运行你的函数后，矩阵变为：
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
# 解释:
# 
# 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O'
# 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
# 
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])

        def dfs(x,y):
            board[x][y] = "B"
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                next_x,next_y = x+dx,y+dy
                if 1 <= next_x < row  and 1 <= next_y < col and board[next_x][next_y] == "O":
                    dfs(next_x,next_y)
        

        for j in range(col):
            if board[0][j] == "O":
                dfs(0,j)
            if board[row-1][j] == "O":
                dfs(row-1,j)

        for i in range(row):
            if board[i][0] == "O":
                dfs(i,0)
            if board[i][col-1] == "O":
                dfs(i,col-1)
        
        for x in range(row):
            for y in range(col):
                if board[x][y] == "O":
                    board[x][y] = "X"
                if board[x][y] == "B":
                    board[x][y] = "O"

# @lc code=end

