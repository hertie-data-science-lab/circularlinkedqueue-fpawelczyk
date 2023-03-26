# -*- coding: utf-8 -*-
"""
Date: Feb 26th 2023
@author: Juan Pablo Brasdefer [225936] (juanbrasdefer) Fabian Pawelczyk [226921] (fpawelczyk)
"""

class Node:
    """A lightweight class for storing a singly linked node."""
    def __init__(self, element, next_node):
        self.element = element
        self.next = next_node


class CircularQueue:
    """Queue implementation using a circularly linked list for storage."""

    def __init__(self):
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        if self.is_empty():
            return "Oh no, the queue is empty! 😢"

        result = []
        current = self.tail.next
        for _ in range(self.size):
            result.append(str(current.element))
            current = current.next

        return " 🎉 -> ".join(result) + " 🎉"

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            raise Exception("Oops! The queue is empty. 🚀")

        return self.tail.next.element

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty. There's nothing to dequeue! 😲")

        old_head = self.tail.next

        if self.size == 1:
            self.tail = None
        else:
            self.tail.next = old_head.next

        self.size -= 1
        return old_head.element

    def enqueue(self, element):
        new_node = Node(element, None)

        if self.is_empty():
            new_node.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node

        self.tail = new_node
        self.size += 1

    def rotate(self):
        if self.size > 0:
            self.tail = self.tail.next

    def clear(self):
        self.tail = None
        self.size = 0
