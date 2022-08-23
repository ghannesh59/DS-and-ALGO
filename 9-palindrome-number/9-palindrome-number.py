class Solution:
    def isPalindrome(self, x: int) -> bool:
        res=list(str(x))
        res=res[::-1]
        print(res)
        return ("".join(res))==str(x)