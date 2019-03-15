#!/usr/bin/env python
# coding: utf-8


def revert_linked_list(head):
    """
    A -> B -> C should become: C -> B -> A
    :param head: LLNode
    :return: new_head: LLNode
    """
    tail = None
    while head:
        head.next_node, tail, head = tail, head, head.next_node
    return tail
