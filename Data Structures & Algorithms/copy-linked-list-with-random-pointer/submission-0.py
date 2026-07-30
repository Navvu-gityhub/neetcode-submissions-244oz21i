"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oc={None:None}
        curr=head
        while curr:
            copy=Node(curr.val)
            oc[curr]=copy
            curr=curr.next
        curr=head
        while curr:
            copy=oc[curr]
            copy.next=oc[curr.next]
            copy.random=oc[curr.random]
            curr=curr.next
        return oc[head]