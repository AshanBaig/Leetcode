# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        temp=lists[0]
        for i in range(1,len(lists)):
            temp=self.mergeTwoLists(temp,lists[i])
        return temp    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        if list1.val<=list2.val:
                head=list1
                list1=list1.next
        else:
            head=list2
            list2=list2.next
        list3=head
        while list1 is not None and list2 is not None:
            if list1.val<=list2.val:
                list3.next=list1
                list1=list1.next
                list3=list3.next
            else:
                list3.next=list2
                list2=list2.next
                list3=list3.next
        while list1 is not None:
            list3.next=list1
            list1=list1.next
            list3=list3.next    
        while list2 is not None:
            list3.next=list2
            list2=list2.next
            list3=list3.next    
        return head