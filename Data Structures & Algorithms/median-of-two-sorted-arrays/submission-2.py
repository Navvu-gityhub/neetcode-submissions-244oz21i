class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        h,j=nums1,nums2
        t=len(nums1)+len(nums2)
        half=t//2
        if len(h)>len(j):
            h,j=j,h
        left,right=0,len(h)-1
        while True:
            o=(left+right)//2
            u=half-o-2
            hl=h[o] if (o)>=0 else float("-infinity")
            hr=h[o+1] if (o+1)<len(h) else float("infinity")
            jl=j[u] if (u)>=0 else float("-infinity")
            jr=j[u+1] if (u+1)<len(j) else float("infinity")
            if hl<=jr and jl<=hr:
                if t%2:
                    return min(hr,jr)
                return (min(hr,jr)+max(hl,jl))/2
            elif hl>jr:
                right=o-1
            else:
                left=o+1