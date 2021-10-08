from Chapter_09.Examples_C09.PriorityQueueBase import PriorityQueueBase
from Chapter_07.Examples_C07.PositionalList import PositionalList


class UnsortedPriorityQueue(PriorityQueueBase):  # Base class defines _Item
    """A min-oriented priority queue implemented with an unsorted list."""

    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def _find_min(self):
        """Return Position of item with minmum key."""
        if self.is_empty():
            raise Empty('Priority queue is empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def add(self, key, value):
        """Add a key-value pair."""
        self._data.add_last(self._Item(key, value))

    def min(self):
        """Return but do not remove (k, v) tuple with minimum key."""
        p = self._find_min()
        item = p.element()
        return item._key, item._value

    def remove_min(self):
        """Remove and rerturn (k, v) tuple with minimum key."""
        p = self._find_min()
        item = self._data.delete(p)
        return item._key, item._value

