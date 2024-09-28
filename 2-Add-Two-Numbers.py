# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=''
        while l1 is not None:
            s1+=str(l1.val)
            l1=l1.next
        s2=''
        while l2 is not None:
            s2+=str(l2.val)
            l2=l2.next
        n1=int(s1[::-1])
        n2=int(s2[::-1])
        s3=str(n1+n2)[::-1]
        head=ListNode(int(s3[0]))
        a=head
        for i in range(1,len(s3)):
            n=ListNode(int(s3[i]))
            a.next=n
            a=n
        return head