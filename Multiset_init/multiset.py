"""
Class implementing multiset
Created Nov 2, 2020
Updated Feb 7, 2024
by Giulio Iannello
"""
from copy import deepcopy


class MultiSet(object):

    def __init__(self, lis=[]):
        "dictionary"
        self.elements = {}
        for item in lis:
            if item not in self.elements.keys():
                self.elements[item] = lis.count(item)

    def add(self, e):
        """
        add an element to the multiset

        Parameters
        ----------
        e : any hashable type
            element to be added.

        Returns
        -------
        None.

        """
        if e in self.elements.keys():
            self.elements[e] += 1
        else:
            self.elements[e] = 1

    def remove(self, e):
        """
        decrease multiplicity of an element if it is > 0

        Parameters
        ----------
        e : any hashable type
            element whose multiplicity must be decreased

        Returns
        -------
        None.

        """
        if e not in self.elements.keys():
            print("L'elemento non è presente nel multiset.")
        else:
            self.elements[e] -= 1
            if self.elements[e] == 0:
                self.elements.pop(e)

    def membership_test(self, e):
        """
        returns True if element e has multiplicity >= 1

        Parameters
        ----------
        e : any hashable type
            element to be checked.

        Returns
        -------
        Boolean
            if element e has multiplicity >= 1

        """
        Membership = False
        if e in self.elements.keys():
            Membership = True
        return Membership

    def union(self, ms):
        """
        return the multiset which is the union
        of the object with multiset ms

        Parameters
        ----------
        ms : Multiset
            multiset to be joined

        Returns
        -------
        new_ms : Multiset
            the union between the object and ms
        """
        new_ms = deepcopy(self)
        for item in ms.elements.keys():
            if new_ms.membership_test(item):
                new_ms.elements[item] += ms.elements[item]
            else:
                new_ms.elements[item] = ms.elements[item]
        return new_ms

    def intersection(self, ms):
        """
        return the multiset which is the itersection
        of the object with multiset ms

        Parameters
        ----------
        ms : Multiset
            multiset to be intersected

        Returns
        -------
        new_ms : Multiset
            the intersection between the object and ms
        """
        new_ms = MultiSet()
        for item in ms.elements.keys():
            if self.membership_test(item):
                new_ms.elements[item] = min(ms.elements[item], self.elements[item])
        return new_ms

    def difference(self,ms):
        """
        return the multiset which is the difference
        of the object with multiset ms

        Parameters
        ----------
        ms : Multiset
            multiset to be subtracted

        Returns
        -------
        new_ms : Multiset
            the difference between the object and ms
        """
        new_ms = deepcopy(self)
        for item in ms.elements.keys():
            if new_ms.membership_test(item):
                new_ms.elements[item] -= ms.elements[item]
                if new_ms.elements[item] < 1:
                    new_ms.elements.pop(item)
        return new_ms
                    


if __name__ == "__main__":
    ms1 = MultiSet([1, 1, 2, 4])        # ms1 = { 1, 1, 2,          4       }
    ms1.add(3)                          # ms1 = { 1, 1, 2,    3,    4       }
    ms1.add(3)                          # ms1 = { 1, 1, 2,    3, 3, 4       }
    ms1.add(2)                          # ms1 = { 1, 1, 2, 2, 3, 3, 4       }
    ms1.remove(1)                       # ms1 = { 1,    2, 2, 3, 3, 4       }
    ms2 = ms1.union(MultiSet([4,5]))    # ms2 = { 1,    2, 2, 3, 3, 4, 4, 5 }
    ms2.remove(2)                       # ms2 = { 1,    2,    3, 3, 4, 4, 5 }
    ms3 = ms1.intersection(ms2)         # ms3 = { 1,    2,    3, 3, 4       }
    ms1 = ms1.difference(ms3)                 # ms1 = {       2                   }
    print(ms1.membership_test(2))       # True
    print(ms1.membership_test(5))       # False
    
    print('Fine')