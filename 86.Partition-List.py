# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        one, two = ListNode(), ListNode()
        ptr1, ptr2 = one, two

        curr = head
        while curr:
            if curr.val < x:
                ptr1.next = curr
                ptr1 = ptr1.next
            else:
                ptr2.next = curr
                ptr2 = ptr2.next
            curr = curr.next

        ptr2.next = None
        ptr1.next = two.next
        return one.next
