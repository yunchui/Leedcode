#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
# https://leetcode-cn.com/problems/word-search/description/
#
# algorithms
# Medium (41.50%)
# Likes:    413
# Dislikes: 0
# Total Accepted:    59.4K
# Total Submissions: 143.1K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
# 
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
# 
# 
# 
# 示例:
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false
# 
# 
# 
# 提示：
# 
# 
# board 和 word 中只包含大写和小写英文字母。
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3
# 
# 
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        n = len(board)
        m = len(board[0])
        visited = [[0 for _ in range(m)] for _ in  range(n)]

        def searchWord(x,y,index):
            print(index)
            if index >= len(word) - 1:
                return board[x][y] == word[index]

            if board[x][y] == word[index]:
                visited[x][y] = 1
            for dx,dy in [[-1,0],[1,0],[0,1],[0,-1]]:
                new_x,new_y = x+dx,y+dy
                if 0 <= new_x < m and 0 <= new_y < n and visited[new_x][new_y] == 0:
                    searchWord(new_x,new_y,index+1)
                    return True
                
            visited[x][y] == 0
            return False
        for x in range(n):
            for y in range(m):
                if searchWord(x,y,0):
                    return True
        return False
                 



# @lc code=end

