class Solution(object):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """            
        def dfs_helper(self,image,visited,sr,sc,color,original_value):
            if sr>=len(image) or sc>=len(image[0]) or sr<0 or sc<0 or visited[sr][sc]==True or image[sr][sc]!=original_value:
                return
            if visited[sr][sc]==False:
                visited[sr][sc]=True
                if image[sr][sc]==original_value:
                    image[sr][sc]=color
            self.dfs_helper(image,visited,sr+1,sc,color,original_value)
            self.dfs_helper(image,visited,sr,sc+1,color,original_value)
            self.dfs_helper(image,visited,sr-1,sc,color,original_value)
            self.dfs_helper(image,visited,sr,sc-1,color,original_value)
        def floodFill(self, image, sr, sc, color):
            visited=[[False for i in range(len(image[0]))]for i in range(len(image))]
            original_value=image[sr][sc]
            self.dfs_helper(image,visited,sr,sc,color,original_value)
            return image