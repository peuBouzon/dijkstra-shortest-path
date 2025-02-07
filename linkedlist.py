from dataclasses import dataclass
from linkedlist import LinkedList

class LinkedList:

    @dataclass
    class Node:
        item: object
        next: LinkedList.Node

    