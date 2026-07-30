# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s,f=head,head.next
        while f and f.next:
            s=s.next
            f=f.next.next
        sec=s.next
        prev=s.next=None
        while sec:
            temp=sec.next
            sec.next=prev
            prev=sec
            sec=temp
        first,sec=head,prev
        while sec:
            t1,t2=first.next,sec.next
            first.next=sec
            sec.next=t1
            first,sec=t1,t2
        