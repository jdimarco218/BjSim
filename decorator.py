#!/usr/bin/env python
from __future__ import print_function
from functools import wraps

from Card import *
from Deck import *

class outerClass(object):
    def __init__(self):
        self.outerList = listHolder()
        self.count_sum = 0
        self.outerList.popFront = self.counter(self.outerList.popFront)

    def keepCount(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            currSum = self.outerList.func(*args, **kwargs)
            print(str(currSum))
        return wrapper

    def counter(self, fn):
        def wrapped(*args, **kwargs):
            card = fn(*args, **kwargs)
            if card.rank < 7:
                self.count_sum -= 1
            elif card.rank < 10:
                pass
            else:
                self.count_sum += 1
            return card
        return wrapped

class listHolder(object):
    def __init__(self):
        self.list_member = []
        self.list_member.append(Card(1, 2))
        self.list_member.append(Card(1, 6))
        self.list_member.append(Card(1, 3))
        self.list_member.append(Card(1, 8))
        self.list_member.append(Card(1, 13))
        self.popped_sum = 0

    def popFront(self):
        return self.list_member.pop(0)


myListHolder = outerClass()

print(str(myListHolder.outerList.popFront()))
print(str(myListHolder.outerList.popFront()))
print(str(myListHolder.outerList.popFront()))
print(str(myListHolder.outerList.popFront()))
print(str(myListHolder.outerList.popFront()))
print(str(myListHolder.count_sum))


