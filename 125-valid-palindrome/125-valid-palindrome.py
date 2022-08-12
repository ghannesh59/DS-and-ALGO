class Solution:
    def isPalindrome(self, s: str) -> bool:
        result_string=''
        for i in s:
            if 97<=ord(i)<=122 or 65<=ord(i)<=90 or i.isdigit():
                result_string=result_string+i
        result_string=result_string.lower()
        i,j=0,len(result_string)-1
        while(i<=j):
            if result_string[i]!=result_string[j]:
                return False
            i=i+1
            j=j-1
        return True
            
        
                
            
        