class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        window, countT = {},{}
        res,resLen = [-1,-1], float("infinity")
        l=0
        for c in t:
            countT[c]=1+ countT.get(c,0)
        have= 0
        need=len(countT)
        for r in range(len(s)):
            c = s[r]
            window[c]=1+window.get(c,0)
            if c in countT and window[c]==countT[c]:
                have+=1
            while have==need:
                curlen=(r-l+1)
                if curlen<resLen:
                    res=[l,r]
                    resLen=curlen
                d=s[l]
                window[d] -=1
                if d in countT and window[d]<countT[d]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""