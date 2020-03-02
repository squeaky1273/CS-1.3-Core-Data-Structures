from hashtable import HashTable

class Set:
    def __init__(self, elements=None):
        """initialize a new empty set structure, and add each element if a sequence is given"""
        self.hash_set = HashTable()

        if elements is not None:
            for element in elements:
                self.add(element)

    # def is_empty(self):
    #     return self.size == 0

    def size(self):
        return self.hash_set.size

    def contains(self, element):
        """return a boolean indicating whether element is in this set
        Running time: O(1); Hash tables work in constant time
        Space(memory): """
        return self.hash_set.contains(element)

    def add(self, element):
        """add element to this set, if not present already
        Running time: O(1); Hash tables use key and value pairs
        Space(memory): """
        if not self.hash_set.contains(element):
            self.hash_set.set(element, 1)

    def remove(self, element):
        """remove element from this set, if present, or else raise KeyError
        Running time: O(1); Items in the table are access in constant time
        Space(memory): """
        if self.hash_set.contains(element):
            self.hash_set.delete(element)
        else:
            raise ValueError('Item not found: {}'.format(element))

    def union(self, other_set):
        """return a new set that is the union of this set and other_set
        Running time: O(n); It takes linear time to get keys
        Space(memory): """
        #new set
        new_set = Set()
        #old sets
        this = self.hash_set.keys()
        other = other_set.hash_set.keys()

        for element in this:
            new_set.add(element)
        for element in other:
            new_set.add(element)

        return new_set

    def intersection(self, other_set):
        """return a new set that is the intersection of this set and other_set
        Running time: O(n); It takes linear time to get keys
        Space(memory): """
        # new set
        new_set = Set()
        # old sets
        # this = self.hash_set.keys()
        other = other_set.hash_set.keys()

        # for element in this:
        #     if other_set.contains(element):
        #         new_set.add(element)
        for element in other:
            if self.contains(element):
                new_set.add(element)

        return new_set

    def difference(self, other_set):
        """return a new set that is the difference of this set and other_set
        Running time: O(n); key method are conducted in linear time.
        Space(memory): """
        # new set
        new_set = Set()
        # old sets
        this = self.hash_set.keys()
        other = other_set.hash_set.keys()

        for element in this:
            if other_set.contains(element) is False:
                new_set.add(element)
        for element in other:
            if self.contains(element) is False:
                new_set.add(element)

        return new_set

    def is_subset(self, other_set):
        """return a boolean indicating whether other_set is a subset of this set
        Running time: O(n); key method are conducted in linear time.
        Space(memory): """
        # old sets
        this = self.hash_set.keys()
        other = other_set.hash_set.keys()

        for element in other:
            if element not in this:
                return False
        return True