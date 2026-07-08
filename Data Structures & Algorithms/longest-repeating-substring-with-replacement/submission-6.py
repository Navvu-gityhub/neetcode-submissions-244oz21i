class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chr={}
        l,res,maxf=0,0,0
        for r in range(len(s)):
            chr[s[r]]=1+chr.get(s[r],0)
            maxf=max(maxf,chr[s[r]])
            while (r-l+1)-maxf>k:
                chr[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res