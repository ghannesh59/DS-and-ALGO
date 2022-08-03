class Solution:
    def myAtoi(self, s: str) -> int:
        max_int=2**31-1
        min_int=-2**31
        result=0
        i=0
        negative=1
        if len(s)<=0:
            return 0
        while (i<len(s) and s[i]==' ') :
            i=i+1
        if i<len(s) and (s[i]=='-' or s[i]=='+') :
            if s[i]=='-':
                negative=-1
            i=i+1
        checker=set('0123456789')
        while (i<len(s) and s[i] in checker):
            result=result*10+int(s[i])
            i=i+1
        result=negative*result
        if negative==-1:
            return max(result,min_int)
        else:
            return min(result,max_int)