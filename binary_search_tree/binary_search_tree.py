import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        else:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
            else: return False
        elif target < self.value:
            if self.left is not None:
                return self.left.contains(target)
            else: return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
    #     cb(self.value)
    #     if self.right is not None:
    #         self.right.for_each(cb)
    #     if self.left is not None:
    #         self.left.for_each(cb)
        s = Stack()
        s.push(self)
        while s.len() > 0:
            current_node = s.pop()
            if current_node.right:
                s.push(current_node.right)
            if current_node.left:
                s.push(current_node.left)
            cb(current_node.value)
    
    


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        
        if self.left is None:
            print(self.value)
        else:
            self.left.in_order_print(self.left)
            print(self.value)
        if self.right is not None:
            self.right.in_order_print(self.right)
        
            

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)
        while(q.len() > 0):
            if q.storage.tail.value.left is not None:
                q.enqueue(q.storage.tail.value.left)
            if q.storage.tail.value.right is not None:
                q.enqueue(q.storage.tail.value.right)
            print(q.dequeue().value)
        

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        s = Stack()
        s.push(self)
        while s.len() > 0:
            current_node = s.pop()
            if current_node.right:
                s.push(current_node.right)
            if current_node.left:
                s.push(current_node.left)
            print(current_node.value)


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass



# bst = BinarySearchTree(1)
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.dft_print(bst)

        #   1
        #               8
        #       5 
        #             7
        #         6          