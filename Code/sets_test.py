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

        set1 = Set(['A', 'B', 'C'])
        set2 = Set(['D', 'E',])
        set3 = set1.union(set2)
        assert set3.contains('A') == True
        assert set3.contains('B') == True
        assert set3.contains('C') == True
        assert set3.contains('D') == True
        assert set3.contains('E') == True
        assert set3.size() == 5

        set1 = Set([1, 2])
        set2 = Set([3, 4])
        set3 = set1.union(set2)
        assert set3.contains(1) == True
        assert set3.contains(2) == True
        assert set3.contains(3) == True
        assert set3.contains(4) == True
        assert set3.contains(5) == False
        assert set3.size() == 4

    def test_intersection(self):
        set1 = Set(['a', 'b', 'c'])
        set2 = Set(['c', 'd', 'e'])
        set3 = set1.intersection(set2)
        assert set3.contains('c') == True
        assert set3.size() == 1

        set4 = Set(['E', 'F', 'G'])
        set5 = Set(['G', 'H', 'I'])
        set6 = set4.intersection(set5)
        assert set6.contains('G') == True
        assert set6.size() == 1

        set7 = Set([1, 2, 3])
        set8 = Set([3, 4, 5])
        set9 = set7.intersection(set8)
        assert set9.contains(3) == True
        assert set9.size() == 1

    def test_difference(self):
        set1 = Set(['a', 'b', 'c'])
        set2 = Set(['c', 'd', 'e'])
        set3 = set1.difference(set2)
        assert set3.contains('a') == True
        assert set3.contains('b') == True
        assert set3.contains('d') == True
        assert set3.contains('e') == True
        assert set3.size() == 4

        set4 = Set(['E', 'F', 'G'])
        set5 = Set(['G', 'H', 'I'])
        set6 = set4.difference(set5)
        assert set6.contains('E') == True
        assert set6.contains('F') == True
        assert set6.contains('H') == True
        assert set6.contains('I') == True
        assert set6.size() == 4

        set7 = Set([1, 2, 3])
        set8 = Set([3, 4, 5])
        set9 = set7.difference(set8)
        assert set9.contains(1) == True
        assert set9.contains(2) == True
        assert set9.contains(4) == True
        assert set9.contains(5) == True
        assert set9.size() == 4

    def test_is_subset(self):
        set1 = Set(['a', 'b', 'c'])
        set2 = Set(['c', 'd'])
        assert set1.is_subset(set2) == False

        set3 = Set(['E', 'F', 'G'])
        set4 = Set(['E', 'F'])
        assert set3.is_subset(set4) == True

        set5 = Set([1, 2, 3])
        set6 = Set([1, 2])
        assert set5.is_subset(set6) == True

if __name__ == '__main__':
    unittest.main()