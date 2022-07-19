class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start=0
        max=0
        for end in range(1,len(prices)):
            if prices[start]>=prices[end]:
                start=end
            else:
                val=prices[end]-prices[start]
                if val>max:
                    max=val
        return max
                
    
            

