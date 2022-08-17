class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count=0
        rows,cols=len(grid),len(grid[0])
        visited=[[False for i in range(cols)] for j in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and visited[r][c]==False:
                    self.dfs(r,c,grid,visited)
                    count=count+1
        return count
    def dfs(self,i,j,grid,visited):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]=="0" or visited[i][j]==True:
            return
        visited[i][j]=True
        for i,j in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
            self.dfs(i,j,grid,visited)