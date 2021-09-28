# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes=[]
        while head:
            nodes.append(head)
            head=head.next
        h=nodes.pop(0)
        while nodes:
            try:
                t=nodes.pop()
                h.next,h=t,t
                t=nodes.pop(0)
                h.next,h=t,t
            except:
                continue
        h.next=None

