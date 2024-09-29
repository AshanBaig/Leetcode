# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return head.next
        def count_el(head):
            count=0
            while head is not None:
                count+=1
                head=head.next
            return count
        a=head
        while a is not None:
            if count_el(a)==n+1:
                a.next=a.next.next
                return head
            a=a.next
        return head.next