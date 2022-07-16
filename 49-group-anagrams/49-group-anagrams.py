class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output=[]
        anagram_dict={}
        for i in strs:
            val=''.join(sorted(i))
            if val not in anagram_dict:
                anagram_dict[val]=[i]
            else:
                anagram_dict[val].append(i)
        for i in anagram_dict:
            output.append(anagram_dict[i])
        return output
    #T.C:O(nlogn)