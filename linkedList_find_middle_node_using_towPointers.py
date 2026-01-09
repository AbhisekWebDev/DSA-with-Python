# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):

        self.val = val
        self.next = next

class Solution:

    def create_linked_list(self, arr):
        
        if not arr:
            return None
        
        head = ListNode(arr[0])
        curr = head
        
        for value in arr[1:]:
            curr.next = ListNode(value)
            curr = curr.next
        
        return head

    def middleNode(self, head) :

        # two pointer method
        slow = head
        fast = head

        while fast != None and fast.next != None :

            slow = slow.next
            fast = fast.next.next
        
        return slow

sol = Solution()

head = sol.create_linked_list([1, 2, 3, 4])

middle = sol.middleNode(head)

print(middle.val)