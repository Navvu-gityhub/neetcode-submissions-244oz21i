# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dum=ListNode(0,head)
        L=dum
        R=head
        while n>0 and R:
            R=R.next
            n-=1
        while R:
            L=L.next
            R=R.next
        L.next=L.next.next
        return dum.next