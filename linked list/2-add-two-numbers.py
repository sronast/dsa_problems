# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        backup = ListNode()
        head = backup
        c = 0
        while l1 or l2 or c:
            res = 0
            if l1:
                res +=l1.val
                l1 = l1.next
            if l2: 
                res += l2.val
                l2 = l2.next
            if c:
                res +=c
            
            if res>=10:
                c = 1
                res -= 10
            else:
                c = 0
            head.next = ListNode(res)
            head = head.next
        return backup.next
                