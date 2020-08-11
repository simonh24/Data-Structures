"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        if self.length == 0:
            self.head = ListNode(value)
            self.tail = ListNode(value)
        else:
            self.head.prev = ListNode(value, None, self.head)
            self.head = self.head.prev
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.length == 1:
            temp = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        elif self.length == 0:
            pass
        else:
            self.length -= 1
            self.head.next.prev = None
            self.head = self.head.next
            return self.head
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.length == 0:
            self.head = ListNode(value)
            self.tail = ListNode(value)
        else:
            self.tail.next = ListNode(value, self.tail, None)
            self.tail = self.tail.next
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length == 1:
            temp = self.tail.value
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        elif self.length == 0:
            pass
        else:
            self.length -= 1
            self.tail.prev.next = None
            self.tail = self.tail.prev
            return self.tail
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        # temp = self.head
        # while temp is not None:
        #     if node.value == temp.value:
        #         break
        #     temp = temp.next
        # self.add_to_head(temp.value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        temp = self.head
        while not temp.value == node.value:
            temp = temp.next
        if temp.next is not None:
            temp.next.prev = temp.prev
        if temp.prev is not None:
            temp.prev.next = temp.next
        if self.length == 1:
            self.head = None
            self.tail = None
        self.length -= 1
        
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max_val = self.head.value
        temp = self.head
        while temp is not None:
            if temp.value > max_val:
                max_val = temp.value
            temp = temp.next
        return max_val