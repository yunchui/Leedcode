#
# @lc app=leetcode.cn id=886 lang=python3
#
# [886] 可能的二分法
#
# https://leetcode-cn.com/problems/possible-bipartition/description/
#
# algorithms
# Medium (39.64%)
# Likes:    62
# Dislikes: 0
# Total Accepted:    4.3K
# Total Submissions: 10.9K
# Testcase Example:  '4\n[[1,2],[1,3],[2,4]]'
#
# 给定一组 N 人（编号为 1, 2, ..., N）， 我们想把每个人分进任意大小的两组。
# 
# 每个人都可能不喜欢其他人，那么他们不应该属于同一组。
# 
# 形式上，如果 dislikes[i] = [a, b]，表示不允许将编号为 a 和 b 的人归入同一组。
# 
# 当可以用这种方法将每个人分进两组时，返回 true；否则返回 false。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：N = 4, dislikes = [[1,2],[1,3],[2,4]]
# 输出：true
# 解释：group1 [1,4], group2 [2,3]
# 
# 
# 示例 2：
# 
# 输入：N = 3, dislikes = [[1,2],[1,3],[2,3]]
# 输出：false
# 
# 
# 示例 3：
# 
# 输入：N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= N <= 2000
# 0 <= dislikes.length <= 10000
# dislikes[i].length == 2
# 1 <= dislikes[i][j] <= N
# dislikes[i][0] < dislikes[i][1]
# 对于 dislikes[i] == dislikes[j] 不存在 i != j
# 
# 
#

# @lc code=start
class Solution:
    '''
    def dfs(self,grid,colors,i,color,n):#染色与i 有关联的，并判断
        colors[i] = color
        for j in range(n):
            if grid[i][j] == 1: #j与i有关联
                if colors[j] == color:#j已经染色且染色相同
                    return False
                if colors[j] == 0 and not self.dfs(grid,colors,j,-1 * color,n):#当前未染色，递归下去，并且染上另一种颜色-1
                    return False
        return True
    


    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        #n = len(dislikes)
        grid = [[0]*N for _ in range(N)]
        colors = [0] * N
        for a,b in dislikes:
            grid[a-1][b-1] = 1
            grid[b-1][a-1] = 1
        for i in range(N):
            #if colors[i] == 0 and not self.dfs(grid,colors,i,1,N):
                return False
        return True
    '''
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        #n = len(dislikes)
        grid = [[0]*N for _ in range(N)]
        colors = [0] * N
        q = collections.deque()
        color = 1
        for a,b in dislikes:
            grid[a-1][b-1] = 1
            grid[b-1][a-1] = 1
        for i in range(N):
            q.append(i)
            if colors[i] == 0:
                colors[i] = color
            while q:
                node = q.popleft()
                for j in range(N):
                    if grid[node][j] == 1:
                        
                        if colors[j] == colors[node]:
                            return False
                        if colors[j] == 0:
                            q.append(j)
                            colors[j] = -1 *colors[node]
                        
        return True
        
    
# @lc code=end

