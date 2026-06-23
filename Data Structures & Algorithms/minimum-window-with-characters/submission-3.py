class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""
        havemap,needmap={},{}
        for c in t:
            needmap[c]=1+needmap.get(c,0)
        have,need=0,len(needmap)
        res,reslen=[-1,-1],float("infinity")
        l=0
        for r in range(len(s)):
            c=s[r]
            havemap[c] = 1+havemap.get(c,0)
            if c in needmap and havemap[c]==needmap[c]:
                have+=1
            while have == need:
                winlen=(r-l+1)
                if winlen<reslen:
                    res=[l,r]
                    reslen=winlen
                d=s[l]
                havemap[d] -= 1
                if d in needmap and havemap[d]<needmap[d]:
                    have-=1
                l+=1
        if reslen == float("infinity"):
            return ""
        else:
            l,r=res
            return s[l:r+1]
        

