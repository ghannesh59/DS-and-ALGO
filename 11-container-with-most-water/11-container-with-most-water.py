class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans,i,j=0,0,len(height)-1
        while(i<j):
            if height[i]<=height[j]:
                result=height[i]*(j-i)
                i=i+1
            else:
                result=height[j]*(j-i)
                j=j-1
            if result>ans:
                ans=result
        return ans
            