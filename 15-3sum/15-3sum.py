
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        nums.insert(0,2^32)
        res=[]
        for i in range(1,len(nums)-1):
            if nums[i]!=nums[i-1]:
                l,r=i+1,len(nums)-1
                while(l<r):
                    value=nums[i]+nums[l]+nums[r]
                    if value<0:
                        l=l+1
                    elif value>0:
                        r=r-1
                    else:
                        res.append([nums[l],nums[i],nums[r]])
                        l=l+1
                        while(l!=len(nums)-1 and nums[l]==nums[l-1]):
                            l=l+1
        return res