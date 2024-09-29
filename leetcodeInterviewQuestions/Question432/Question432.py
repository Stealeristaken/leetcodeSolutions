class Node:
    def __init__(self):
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        self.key_to_count = {}  # Maps key to its count
        self.count_to_node = {}  # Maps count to its node in the linked list
        self.head = Node()  # Dummy head of the doubly linked list
        self.tail = Node()  # Dummy tail of the doubly linked list
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node_after(self, new_node, prev_node):
        """Add new_node after prev_node."""
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = next_node
        next_node.prev = new_node

    def _remove_node(self, node):
        """Remove a node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _get_node(self, count):
        """Returns the node for a specific count, creating it if it doesn't exist."""
        if count not in self.count_to_node:
            new_node = Node()
            self.count_to_node[count] = new_node
        return self.count_to_node[count]

    def inc(self, key: str) -> None:
        """Increments the count of a key by 1."""
        if key in self.key_to_count:
            current_count = self.key_to_count[key]
            new_count = current_count + 1
            self.key_to_count[key] = new_count

            # Move the key from current_count to new_count in the linked list
            current_node = self.count_to_node[current_count]
            current_node.keys.remove(key)

            if new_count not in self.count_to_node:
                new_node = Node()
                self.count_to_node[new_count] = new_node
                self._add_node_after(new_node, current_node)
            
            self.count_to_node[new_count].keys.add(key)

            # If the old node becomes empty, remove it
            if len(current_node.keys) == 0:
                self._remove_node(current_node)
                del self.count_to_node[current_count]
        else:
            # First occurrence of the key
            self.key_to_count[key] = 1
            if 1 not in self.count_to_node:
                new_node = Node()
                self.count_to_node[1] = new_node
                self._add_node_after(new_node, self.head)
            self.count_to_node[1].keys.add(key)

    def dec(self, key: str) -> None:
        """Decrements the count of a key by 1."""
        if key not in self.key_to_count:
            return

        current_count = self.key_to_count[key]
        new_count = current_count - 1

        # Remove the key from the current node
        current_node = self.count_to_node[current_count]
        current_node.keys.remove(key)

        if new_count == 0:
            # Remove the key completely if the new count is 0
            del self.key_to_count[key]
        else:
            # Update the count and move the key to the new node
            self.key_to_count[key] = new_count
            if new_count not in self.count_to_node:
                new_node = Node()
                self.count_to_node[new_count] = new_node
                self._add_node_after(new_node, current_node.prev)
            self.count_to_node[new_count].keys.add(key)

        # If the old node becomes empty, remove it
        if len(current_node.keys) == 0:
            self._remove_node(current_node)
            del self.count_to_node[current_count]

    def getMaxKey(self) -> str:
        """Returns one of the keys with the maximal count."""
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        """Returns one of the keys with the minimal count."""
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))