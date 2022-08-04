class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        res=0
        seen={}
        for end in range(len(s)):
            if s[end] not in seen:
                res=max(res,(end-start)+1)
            else:
                if seen[s[end]]<start:
                    res=max(res,(end-start)+1)
                else:
                    start=seen[s[end]]+1
            seen[s[end]]=end
        return res


                