from hashtable import HashTable

class Set:
    def _init_(self, elements=None):
        """initialize a new empty set structure, and add each element if a sequence is given"""
        self.size = 0
        self.hash = HashTable()
        pass

    def contains(self, element):
        """return a boolean indicating whether element is in this set
        Running time: O(1); 
        Space(memory): """
        return self.hash.contains(element) is True

    def add(self, element):
        """add element to this set, if not present already
        Running time: O(1); 
        Space(memory): """
        if self.hash.contains(element):
            return('Already in set')
        else:
            self.hash.set(element, None)
            self.size += 1

    def remove(self, element):
        """remove element from this set, if present, or else raise KeyError
        Running time: O(1); 
        Space(memory): """
        if self.hash.contains(element):
            self.hash.delete(element)
        else:
            raise ValueError('Item not found: {}'.format(element))

    def union(self, other_set):
        """return a new set that is the union of this set and other_set
        Running time: 
        Space(memory): """
        new_set = Set()
        ...
        return new_set

    def intersection(self, other_set):
        """return a new set that is the intersection of this set and other_set
        Running time: 
        Space(memory): """
        new_set = Set()
        ...
        return new_set

    def difference(self, other_set):
        """return a new set that is the difference of this set and other_set
        Running time: 
        Space(memory): """
        new_set = Set()
        ...
        return new_set

    def is_subset(self, other_set):
        """return a boolean indicating whether other_set is a subset of this set
        Running time: 
        Space(memory): """
        return self.is_subset(other_set) is True