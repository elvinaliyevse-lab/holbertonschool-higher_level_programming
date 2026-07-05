#!/usr/bin/python3
"""Module for creating the class named Node and SinglyLinkedList"""


class Node:
    """The class Node and its attributes"""
    def __init__(self, data, next_node=None):
        """Initializing attributes"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for data"""
        return self.__data

    @property
    def next_node(self):
        """Getter for next node"""
        return self.__next_node

    @data.setter
    def data(self, value):
        """Setter for data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """Setter for next_node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """The class for head of single linked list"""
    def __init__(self):
        """Initializing attributes"""
        self.head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if not self.head or self.head.data >= new_node.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and current.next_node.data < new_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        sll = ""
        current = self.head
        while current:
            sll += str(current.data) + "\n"
            current = current.next_node
        return sll.strip()
