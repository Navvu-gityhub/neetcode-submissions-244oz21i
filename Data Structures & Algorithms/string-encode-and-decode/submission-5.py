class Solution:

    def encode(self, strs: List[str]) -> str:
        enc=""
        for s in strs:
            enc+=str(len(s))+"#"+s
        return enc
    def decode(self, s: str) -> List[str]:
        dec=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            dec.append(s[j+1:j+1+length])
            i=1+j+length
        return dec