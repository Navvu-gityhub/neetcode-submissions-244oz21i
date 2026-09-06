class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i : i[0])
        op=[intervals[0]]
        for start,end in intervals[1:]:
            prevEndVal=op[-1][1]
            if start<=prevEndVal:
                op[-1][1]=max(prevEndVal,end)
            else:
                op.append([start,end])
        return op    

        
