class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":return ""
        hmap,nmap={},{}
        for c in t:
            nmap[c]=1+nmap.get(c,0)
        have,need=0,len(nmap)
        l=0
        res,reslen=[-1,-1],float("infinity")
        for r in range(len(s)):
            c=s[r]
            hmap[c]=1+hmap.get(c,0)
            if c in nmap and hmap[c]==nmap[c]:
                have+=1
            while have==need:
                winlen=(r-l+1)
                if winlen<reslen:
                    res=[l,r]
                    reslen=winlen
                d=s[l]
                hmap[d]-=1
                if d in nmap and hmap[d]<nmap[d]:
                    have-=1
                l+=1
        if reslen == float("infinity"):
            return ""
        else:
            l,r=res
            return s[l:r+1]

