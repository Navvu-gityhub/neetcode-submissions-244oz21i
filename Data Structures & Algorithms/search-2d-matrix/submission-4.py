class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        """main=[]
        for i in matrix:
            main+=i


        starting,end=0,len(main)-1

  

        while starting<=end:
            mid= starting+(-starting+end)//2
            if main[mid]>target:
                end=mid-1
            elif target>main[mid]:
                starting=mid+1
            else:
                return True
        
        return False
"""

        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = l + (r - l) // 2
            row, col = m // COLS, m % COLS
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False
        
            

        