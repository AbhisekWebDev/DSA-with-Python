# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

def deleteDuplicates(head) :

    myHash = set()

    temp = head
    prev = None

    while temp :
       
        if temp.val not in myHash :
            myHash.add(temp.val)
            prev = temp # move prev forward
            temp = temp.next # move temp forward
        
        else :
            prev.next = temp.next # delete duplicate
            temp = temp.next # move temp only

    return head

# Helper function to print list
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

def create_linked_list(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    curr = head
    
    for value in arr[1:]:
        curr.next = ListNode(value)
        curr = curr.next
    
    return head

head = create_linked_list([1, 2, 3, 4, 4, 2, 1])

print("Original List:")
printList(head)

print("Removed Duplicates:")
new_head = deleteDuplicates(head)
printList(new_head)