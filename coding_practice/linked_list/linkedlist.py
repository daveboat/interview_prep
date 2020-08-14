class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head_data):
        self.head = Node(head_data)

    def append(self, data):
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = Node(data)

    def traverse(self):
        current_node = self.head

        print(current_node.data)
        while current_node.next is not None:
            current_node = current_node.next
            print(current_node.data)

    def prepend(self, data):
        previous_head = self.head

        self.head = Node(data)

        self.head.next = previous_head

    def detect_loop(self):
        # loop detection in a linked list using floyd's cycle detection algorithm (slow-fast pointers)
        slow = self.head
        fast = self.head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    def detect_and_remove_loop(self):
        # first, detect loop with slow/fast pointers
        slow = self.head
        fast = self.head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        # now, set one pointer to head and keep the other pointer where it is. move them both 1 at a time now. They
        # should meet at the start node of the loop. If we keep track of which node was the previous node of the one
        # that stayed inside the loop, we can set that node's next to None
        if slow == fast:
            slow = self.head
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next

            # set the last node in the loop's next pointer to None. Note that we must set the next of fast to none
            # because it is the one that's in the loop, because we set slow to head. If we set slow.next to none, then
            # we simply excise the loop.
            fast.next = None


if __name__ == '__main__':
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    ll.append(9)
    ll.append(10)

    # create a loop
    ll.head.next.next.next.next.next.next.next.next.next.next = ll.head.next.next.next.next

    print(ll.detect_loop())
    ll.detect_and_remove_loop()

    ll.traverse()
