#!/usr/bin/python3

class pushswap:
    def __init__(self, sort_list, listA, listB, is_printable) -> None:
        self.sort_list = sort_list
        self.listA = listA
        self.listB = listB
        self.len = len(listA) + len(listB)

    def sa(self):
        if len(self.listA) > 1:
            self.listA[0], self.listA[1] = self.listA[1], self.listA[0]

    def sb(self):
        if len(self.listB) > 1:
            self.listB[0], self.listB[1] = self.listB[1], self.listB[0]

    def sc(self):
        self.sb()
        self.sa()

    def pa(self):
        if self.listB:
            self.listA.insert(0, self.listB.pop(0))

    def pb(self):
        if self.listA:
            self.listB.insert(0, self.listA.pop(0))

    def ra(self):
        if len(self.listA) > 1:
            self.listA.extend([self.listA.pop(0)])

    def rb(self):
        if len(self.listB) > 1:
            self.listB.extend([self.listB.pop(0)])

    def rr(self):
        self.ra()
        self.rb()

    def rra(self):
        if len(self.listA) > 1:
            self.listA.append(self.listA.pop(-1))

    def rrb(self):
        if len(self.listA) > 1:
            self.listA.append(self.listA.pop(-1))

    def rrr(self):
        self.rra()
        self.rrb()

    def is_sort(self):
        if len(self.listB) != 0:
            return 0
        listA = sorted(self.listA)
        for i, j in zip(listA, self.listA):
            if i != j:
                return 0
        return 1
