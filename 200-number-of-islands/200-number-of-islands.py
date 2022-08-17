class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid)==0:
            return 0
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    grid[i][j]=0
                    self.bfs(grid,i,j)
                    count=count+1
        return count
    def bfs(self,grid,i,j):
        queue=[]
        queue.append((i,j))
        while(queue):
            i,j=queue.pop(0)
            for i,j in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]=="1":
                    queue.append((i,j))
                    grid[i][j]=0
        