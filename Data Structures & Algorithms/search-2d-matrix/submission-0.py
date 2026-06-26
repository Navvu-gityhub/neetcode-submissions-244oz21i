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
                row=matrix[M]
                l,r=0,len(row)-1
                while l<=r:
                    m=l+((r-l)//2)
                    if row[m]>target:
                        r=m-1
                    elif row[m]<target:
                        l=m+1
                    else:
                        return True
                return False
        return False   