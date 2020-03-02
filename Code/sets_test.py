from sets import Set
import unittest

class SetsTests(unittest.TestCase):
    
    def test_init(self):
        hash_set = Set(['a', 'b', 'c'])
        assert hash_set.size() == 3

    # def test_is_empty(self):
    #     set = Set()
    #     assert set.size == 0

    def test_contains(self):
        hash_set = Set(['a', 'b', 'c'])
        assert hash_set.contains('a') == True
        assert hash_set.contains('b') == True
        assert hash_set.contains('c') == True
        assert hash_set.contains('e') == False
        assert hash_set.contains('f') == False

    def test_add(self):
        hash_set = Set()
        hash_set.add('a') == True
        hash_set.add('b') == True
        hash_set.add('c') == True
        assert hash_set.size() == 3

    def test_remove(self):
        hash_set = Set()
        hash_set.add('a')
        hash_set.add('b')
        assert hash_set.size() == 2
        hash_set.remove('a')
        assert hash_set.size() == 1

    def test_union(self):
        set1 = Set(['a', 'b', 'c'])
        set2 = Set(['d', 'e', 'f'])
        set3 = set1.union(set2)
        assert set3.contains('a') == True
        assert set3.contains('b') == True
        assert set3.contains('c') == True
        assert set3.contains('d') == True
        assert set3.contains('e') == True
        assert set3.contains('f') == True
        assert set3.size() == 6

    def test_intersection(self):
        set1 = Set(['a', 'b', 'c'])
        set2 = Set(['c', 'd', 'e'])
        set3 = set1.intersection(set2)
        assert set3.contains('c') == True
        assert set3.size() == 1

    def test_difference(self):
        set1 = Set(['a', 'b', 'c'])
        set2 = Set(['c', 'd', 'e'])
        set3 = set1.difference(set2)
        assert set3.contains('a') == True
        assert set3.contains('b') == True
        assert set3.contains('d') == True
        assert set3.contains('e') == True
        assert set3.size() == 4

    def test_is_subset(self):
        set1 = Set(['a', 'b', 'c'])
        set2 = Set(['c', 'd'])
        assert set1.is_subset(set2) == False

if __name__ == '__main__':
    unittest.main()