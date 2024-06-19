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
        if not head:
            return head
        lookup = {None:None}
        cur = head
        while cur:
            lookup[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        new_head = lookup[cur]

        while cur:
            new_head.next = lookup[cur.next]
            new_head.random = lookup[cur.random]
            cur = cur.next
            new_head = new_head.next
        return lookup[head]
