"""
File: arraystack.py
Project 7.1
"""

from arrays import Array, ArrayExpanded
from abstractstack import AbstractStack

class ArrayStack(AbstractStack):
    """An array-based stack implementation."""
    DEFAULT_CAPACITY = 100
    
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = ArrayExpanded(ArrayStack.DEFAULT_CAPACITY)
        AbstractStack.__init__(self, sourceCollection)
        
    def __iter__(self):
        """Supports iteration over a view of self.
        Visits items from bottom to top of stack."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def peek(self):
        """Returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if stack is empty."""
        if self.isEmpty():
            raise KeyError("The stack is empty")
        return self._items[len(self) - 1]

    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)

    def push(self, item):
        """Inserts item at top of the stack."""
        print(type(self), self._size)
        if len(self) == len(self._items):
            print("grow")
            self._items.grow()
        self._items[len(self)] = item
        self._size += 1

    def pop(self):
        """Removes and returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if stack is empty.
        Postcondition: the top item is removed from the stack."""
        if self.isEmpty():
            raise KeyError("The stack is empty")
        oldItem = self._items[len(self) - 1]
        self._size -= 1
        if len(self) <= len(self._items) // 4 and \
           len(self._items) >= 2 * ArrayStack.DEFAULT_CAPACITY:
            print("shrink")
            self._items.shrink()
        return oldItem
