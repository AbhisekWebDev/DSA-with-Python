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

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        # This works only when the node is NOT the tail, because:
        node.val = node.next.val
        node.next = node.next.next

    # Helper function to print list
    def printList(self, head):

        while head:
            print(head.val, end=" -> ")
            head = head.next
        
        print("None")

    # Find node by value
    def findNode(self, head, value):
        while head:
            if head.val == value:
                return head
            head = head.next
        return None
    
    # Find node by index
    def getNodeAtIndex(self, head, index):
        curr = head
        i = 0
        
        while curr and i < index:
            curr = curr.next
            i += 1
        
        return curr

sol = Solution()

head = sol.create_linked_list([1, 2, 3, 4])

print("Before deletion:")
sol.printList(head)

node = sol.findNode(head, 2)   # find node with value 2
sol.deleteNode(node)

node = sol.getNodeAtIndex(head, 1)   # find node with index 2
sol.deleteNode(node)

print("After deletion:")
sol.printList(head)




# node = sol.getNodeAtIndex(head, 2)

# if node and node.next:
#     sol.deleteNode(node)
# else:
#     print("Cannot delete tail node using deleteNode")