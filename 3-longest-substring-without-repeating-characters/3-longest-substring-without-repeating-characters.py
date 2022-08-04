class Solution(object):
    def lengthOfLongestSubstring(self, s):
                
        """
        :type s: str
        :rtype: int
        """
        max1=0
        start=0
        end=0
        dict1={}
        set1=set(s)
        if len(set1)==len(s):
            return len(s)
        elif len(s)==0:
            return 0
        else:
            for i in range(len(s)):
                if s[i] in dict1 and dict1[s[i]]>=start:
                        end=end+1
                        start=dict1[s[i]]+1
                        len2=end-start
                        if len2>max1:
                            max1=len2    
                else:
                    end=end+1
                    len3=end-start
                    if len3>max1:
                        max1=len3
                dict1[s[i]]=i
            return max1