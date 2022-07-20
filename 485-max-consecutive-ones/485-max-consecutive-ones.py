class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start=0
        count=0
        for end in range(len(nums)):
            if nums[end]==1:
                count=max(count,(end-start)+1)
            else:
                start=end+1
        return count
            
                
            
            