from Chapter_07.Examples_C07.DoublyLinkedBase import _DoublyLinkedBase
from empty_exception import Empty


class LinkedDeque(_DoublyLinkedBase):
    """Double-ended queue implementation based on a doubly linked list."""

    def first(self):
        """Return (but do not remove) the element at the front of the deque."""
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._header._next._element

    def last(self):
        """Return (but do not remove) the element at the back of the deque."""
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._trailer._prev._element

    def insert_first(self, e):
        """Add an element to the front of the deque."""
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        """Add an element to the back of the deque."""
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """
        Remove and return the element from the back of the deque.
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._header._next)

    def delete_last(self):
        """
        Remove and return the element from the back of the deque.
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._trailer._prev)


if __name__ == "__main__":
    deque = LinkedDeque()
    deque.insert_first('a')
    deque.insert_last('b')
    deque.insert_last('c')
    print(deque.first())
    print(deque.last())
    deque.delete_last()
    print(deque.last())