class Solution:
    def isHappy(self, n: int) -> bool:
        n=str(n)
        sum_dict={}
        while(n not in sum_dict):
            temp=sum([int(i)**2 for i in n])
            sum_dict[n]=temp
            n=str(temp)
        if 1 in sum_dict.values():
            return True
        else:
            return False
    
        
            