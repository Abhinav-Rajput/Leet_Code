# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1=list1
        l2= list2 
        newlist = ListNode(0)
        newlistptr = newlist
 
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                newlistptr.next = l1
                l1 = l1.next
            else:
                newlistptr.next = l2
                l2 = l2.next
            newlistptr = newlistptr.next
        if l1 != None:
            newlistptr.next = l1
        else:
            newlistptr.next = l2
        return newlist.next

        # new1=None
        # while list1 and list2:
        #     if list1.val<list2.val:

        #         if new1 is None:
        #             new1 = ListNode(list1.val)
        #             list1=list1.next
        #         else:
        #             temp = ListNode(list1.val)
        #             new1.next=temp
        #             list1=list1.next
        #     elif list1.val>list2.val:
        #         if new1 is None:
        #             new1 = ListNode(list2.val)
        #             list2=list2.next
        #         else:
        #             temp = ListNode(list2.val)
        #             new1.next=temp
        #             list2=list2.next
        #     else:
        #         if new1 is None:
        #             new1 = ListNode(list2.val)
        #             list2=list2.next

        #             temp = ListNode(list1.val)
        #             new1.next=temp
        #             list1=list1.next
        #         else:
        #             temp = ListNode(list1.val)
        #             new1.next=temp
        #             list1=list1.next

        #             temp = ListNode(list2.val)
        #             new1.next=temp
        #             list2=list2.next
        # return new1

        newList = ListNode(0)
        newListptr = newList

        while list1!=None and list2!=None:

            if list1.val <= list2.val:
                newListptr.next =list1
                list1 = list1.next
            else:
                newListptr.next = list2
                list2 = list2.next
            
            newListptr = newListptr.next
        
        if list1:
            newListptr.next = list1
        else:
            newListptr.next = list2
        
        return newListptr.next






        