#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 14:51:29 2019

@author: andreamansur

Collections
"""

"""
#Python List is built as an array 
#inserting into a list is constant time but beacuse python list
#is and array inserting into an array is linear time O(n), so 
#inserting into a python list is linear time
#search operations are still constant time making len() constant

#Linked List vs array
#array : value and index stored
#linked list: value and pointer to next (memory address)
#doubly linked list : pointer to before and after element
"""

class Element(object):
    def __init__(self, value):#initalize new element
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head = None):#establish new linked list with no head
        self.head = head
    def append(self, new_element):
        current = self.head
        if self.head: #check if a head already exists
            while current.next: #if it does exist then iterate to end of the list
                current = current.next
            current.next = new_element
        else:
            self.head = new_element #if head doesnt exist set it to new element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        count = 1
        current = self.head
        if position >= 1 and position <= length :
            while count < position:
                current = current.next
                count += 1
            return current
        else:
            return "None"