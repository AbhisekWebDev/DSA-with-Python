# Doubly linked list node
class DNode:
    def __init__(self, val = 0) :
        self.val = val
        self.next = None
        self.prev = None

# create doubly linked list
def create_dll(arr):
    if not arr:
        return None
    
    head = DNode(arr[0])
    curr = head

    for value in arr[1:]:
        new_node = DNode(value)
        curr.next = new_node
        new_node.prev = curr
        curr = new_node
    
    return head

head = create_dll([1, 2, 3, 4])

# Print forward
def print_fw(head):
    curr = head
    tail = None

    while curr:
        print(curr.val, end=" <-> ")
        
        if curr.next is None:
            tail = curr   # capture tail for reverse print
        curr = curr.next
    
    print("None")
    
    return tail

# Print backward
def print_bw(tail):
    curr = tail
    
    while curr:
        print(curr.val, end=" <-> ")
        curr = curr.prev
    print("None")

print("Original DLL (Forward):")
tail = print_fw(head) # to never reuse an “old” tail.

print("Backward:")
print_bw(tail)

# Reverse DLL
def reverse_dll(head):
    curr = head
    prev_node = None

    while curr:
        prev_node = curr
        curr.prev, curr.next = curr.next, curr.prev #swap links
        curr = curr.prev  # move to next node (which is prev due to swap)
    
    return prev_node  # new head

print("\nAfter Reversing:")
head = reverse_dll(head)
tail = print_fw(head)
print("Backward:")
print_bw(tail)

# Insert at beginning
def insert_beg(head, val):
    new_node = DNode(val)
    new_node.next = head

    if head:
        head.prev = new_node
    
    return new_node

print("\nInsert at Beginning (0):")
head = insert_beg(head, 6)
tail = print_fw(head)
print("Backward:")
print_bw(tail)

# Insert at end
def insert_end(head, val):
    if not head:
        return DNode(val)
    
    curr = head
    
    while curr.next:
        curr = curr.next
    
    new_node = DNode(val)
    curr.next = new_node
    new_node.prev = curr

    return head

print("\nInsert at End (5):")
head = insert_end(head, 5)
tail = print_fw(head)
print("Backward:")
print_bw(tail)


# Inhsert at pos
def insert_pos(head, pos, val):
    if pos ==0:
        return insert_beg(head, val)
    
    curr = head

    for _ in range(pos - 1):
        if not curr:
            return head
        
        curr = curr.next

    if not curr:
        return head
        
    new_node = DNode(val)
    new_node.next = curr.next
    new_node.prev = curr

    if curr.next:
        curr.next.prev = new_node
        
    curr.next = new_node
    
    return head

print("\nInsert 9 at Position 2:")
head = insert_pos(head, 2, 7)
tail = print_fw(head)
print("Backward:")
print_bw(tail)

# Delete from beginning
def delete_beg(head):
    if not head:
        return None
    
    head = head.next
    
    if head:
        head.prev = None
    
    return head

print("\nDelete from Beginning:")
head = delete_beg(head)
tail = print_fw(head)
print("Backword:")
print_bw(tail)

# Delete from end
def delete_end(head):
    if not head:
        return None
    
    if not head.next:
        return None
    
    curr = head
    
    while curr.next:
        curr = curr.next
    
    curr.prev.next = None
    
    return head

print("\nDelete from End:")
head = delete_end(head)
tail = print_fw(head)
print("Backward:")
print_bw(tail)

# Delete at Position
def delete_pos(head, pos):
    if not head:
        return None
    
    if pos == 0:
        return delete_beg(head)
    
    curr = head
    
    for _ in range(pos):
        if not curr:
            return head
        curr = curr.next
    
    if not curr:
        return head
    
    if curr.next:
        curr.next.prev = curr.prev
    
    curr.prev.next = curr.next
    
    return head

print("\nDelete from Position 2:")
head = delete_pos(head, 2)
tail = print_fw(head)
print("Backward:")
print_bw(tail)
