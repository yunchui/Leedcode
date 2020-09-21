#
# @lc app=leetcode.cn id=785 lang=python3
#
# [785] 判断二分图
#
# https://leetcode-cn.com/problems/is-graph-bipartite/description/
#
# algorithms
# Medium (49.87%)
# Likes:    174
# Dislikes: 0
# Total Accepted:    27.7K
# Total Submissions: 55.5K
# Testcase Example:  '[[1,3],[0,2],[1,3],[0,2]]'
#
# 给定一个无向图graph，当这个图为二分图时返回true。
# 
# 如果我们能将一个图的节点集合分割成两个独立的子集A和B，并使图中的每一条边的两个节点一个来自A集合，一个来自B集合，我们就将这个图称为二分图。
# 
# 
# graph将会以邻接表方式给出，graph[i]表示图中与节点i相连的所有节点。每个节点都是一个在0到graph.length-1之间的整数。这图中没有自环和平行边：
# graph[i] 中不存在i，并且graph[i]中没有重复的值。
# 
# 
# 
# 示例 1:
# 输入: [[1,3], [0,2], [1,3], [0,2]]
# 输出: true
# 解释: 
# 无向图如下:
# 0----1
# |    |
# |    |
# 3----2
# 我们可以将节点分成两组: {0, 2} 和 {1, 3}。
# 
# 
# 
# 
# 示例 2:
# 输入: [[1,2,3], [0,2], [0,1,3], [0,2]]
# 输出: false
# 解释: 
# 无向图如下:
# 0----1
# | \  |
# |  \ |
# 3----2
# 我们不能将节点分割成两个独立的子集。
# 
# 
# 注意:
# 
# 
# graph 的长度范围为 [1, 100]。
# graph[i] 中的元素的范围为 [0, graph.length - 1]。
# graph[i] 不会包含 i 或者有重复的值。
# 图是无向的: 如果j 在 graph[i]里边, 那么 i 也会在 graph[j]里边。
# 
# 
#

# @lc code=start
class Solution:
    '''
    def dfs(self,grid,colors,i,color,n):
        colors[i] = color
        for j in range(n):
            if grid[i][j] == 1:
                if colors[j] == color:
                    return False
                if colors[j] == 0 and not self.dfs(grid,colors,j,-1*color,n):
                    return False
        return True
    '''
    def bfs(self,grid,colors,i,color,n):
        q = collections.deque([i])
        colors[i] = color
        while q:
            node = q.popleft()
            for j in range(n):
                if grid[node][j] == 1:
                    if colors[j] == 0:
                        q.append(j)
                        colors[j] = -1 * colors[node]
                    if colors[j] == colors[node]:
                        return False
        return True


    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        grid = [[0] * n for _ in range(n)]
        colors = [0] * n #全都没标记
        for  i in range(n): #标记所有关联边
            for j  in graph[i]:
                grid[i][j] = 1
        for i in range(n):
            #if colors[i] == 0 and not self.dfs(grid,colors,i,1,n):
            if colors[i] == 0 and not self.bfs(grid,colors,i,1,n):  
                return False
        return True

# @lc code=end

