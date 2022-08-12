class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict1={}
        for i,n in enumerate(numbers):
            m=target-n
            if m in dict1:
                return [dict1[m]+1,i+1]
            else:
                dict1[n]=i