class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chrset=set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in chrset:
                chrset.remove(s[l])
                l+=1
            chrset.add(s[r])
            res=max(res,r-l+1)
        return res