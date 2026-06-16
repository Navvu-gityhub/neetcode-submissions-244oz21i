class Solution:
    def threeSum(self, n: List[int]) -> List[List[int]]:
        res= []
        n.sort()
        for i in range(len(n)):
            if i>0 and n[i]== n[i-1]:
                continue
            l,r=i+1,len(n)-1
            while l<r:
                tsum =n[i]+n[l]+n[r]
                if tsum>0: r-=1
                elif tsum<0: l+=1
                else:
                    res.append([n[i],n[l],n[r]])
                    l+=1
                    while n[l]==n[l-1] and l<r:
                        l+=1
        return res