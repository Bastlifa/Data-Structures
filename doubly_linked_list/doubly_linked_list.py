"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        temp_head = self.head
        self.head = ListNode(value, None, temp_head)
        if temp_head is not None:
            temp_head.prev = self.head
            self.head.next = temp_head
        else:
            self.tail = self.head
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        ret_val = None
        if self.head is not None:
            ret_val = self.head.value
            if self.head.next is not None:
                self.head = self.head.next
                self.head.prev = None
                self.length = self.length - 1
            else:
                self.head = None
                self.tail = None
                self.length = 0
        return ret_val

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        if self.tail is not None:
            temp_tail = self.tail
            self.tail.next = ListNode(value, self.tail)
            self.tail = self.tail.next
            self.tail.prev = temp_tail
            self.length += 1
        else: self.add_to_head(value)

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        ret_val = None
        if self.tail is not None:
            ret_val = self.tail.value
            if self.tail.prev is not None:
                self.tail = self.tail.prev
            else:
                self.tail = None
                self.head = None
            self.length = self.length - 1
        return ret_val

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        self.length -= 1
        self.add_to_head(node.value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        self.length -= 1
        self.add_to_tail(node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if self.length > 1:
            if node.prev and node.next:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.length = max(self.length - 1, 0)
                return
            elif node.prev and not node.next:
                self.remove_from_tail()
                return
            elif not node.prev and node.next:
                self.remove_from_head()
        else: 
            self.head = None
            self.tail = None
            self.length = 0
    """Returns the highest value currently in the list"""
    def get_max(self):
        node = self.head
        max_val = self.head.value
        while node.next:
            node = node.next
            if max_val < node.value:
                max_val = node.value
        
        return max_val
