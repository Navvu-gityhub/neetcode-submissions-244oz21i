"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import heappush, heappop
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        heap=[]
        ans=0
        for i in intervals:
            if heap and i.start>=heap[0]:
                heappop(heap)
            heappush(heap,i.end)
            ans=max(ans,len(heap))
        return ans
