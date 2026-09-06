class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #overlapping curr start< prev end-->count
        #non overlapping curr start > prev end
        intervals.sort(key=lambda i:i[0])
        count=0
        prevEnd=intervals[0][1]
        for start,end in intervals[1:]:
            if start<prevEnd:
                count+=1
                prevEnd=min(end,prevEnd)
            else:
                prevEnd=end
        return count


