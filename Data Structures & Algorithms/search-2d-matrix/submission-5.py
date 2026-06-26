class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L,R=0,len(matrix)-1
        while L<=R:
            M=L+((R-L)//2)
            if target<matrix[M][0]:
                R=M-1
            elif target>matrix[M][-1]:
                L=M+1
            else:
                trow=matrix[M]
                l,r=0,len(trow)-1
                while l<=r:
                    m=l+((r-l)//2)
                    if trow[m]>target:
                        r=m-1
                    elif trow[m]<target:
                        l=m+1
                    else:
                        return True
                return False
        return False