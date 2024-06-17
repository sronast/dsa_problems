    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #split the linked list into two parts
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None

        # Reverse the second list
        prev = None
        while head2:
            temp = head2.next
            head2.next = prev
            prev = head2
            head2 = temp

        #Combine two lists
        head3 = head
        head4 = prev
    
        while head3 and head4:
            temp = head3.next
            head3.next = head4
            head3 = head3.next
            head4 = temp

        return head
        