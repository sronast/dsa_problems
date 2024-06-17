# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        def helper(node):
            if node is None or node.next is None:
                return node
            h = helper(node.next)
            node.next.next = node
            node.next = None
            
            return h

        return helper(head)
