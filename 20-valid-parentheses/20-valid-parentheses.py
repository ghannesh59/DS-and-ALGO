class Solution:
    def isValid(self, s: str) -> bool:
        dict1={'(':')','[':']','{':'}'}
        stack=[]
        for i in s:
            if i in dict1:
                stack.append(i)
            elif len(stack)==0 or dict1[stack.pop()]!=i:
                return False
        return True if len(stack)==0 else False