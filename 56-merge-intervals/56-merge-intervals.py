class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        curr=intervals[0]
        result=[]
        for i in intervals:
            if i[0]<=curr[1]:
                curr[1]=max(curr[1],i[1])
            else:
                result.append(curr)
                curr=i
        result.append(curr)
        return result
                
                
                
        