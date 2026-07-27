# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #dummy node and tail
        head=ListNode()
        d,tail=head,head
        #see if l1 and l2 not null
        while l1 and l2:
            #if l1's value greater than l2's value
            if l1.val<l2.val:
                #update tail's next to l1
                tail.next=l1
                l1=l1.next#update l1 pointer
            else:
                tail.next=l2#if l1=l2 or l1<l2 update tail's next to l2
                l2=l2.next
            tail=tail.next#update tail ptr
        if l1:
            tail.next=l1
        elif l2:
            tail.next=l2
        return d.next
