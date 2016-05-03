"""Test case for sorting"""
import bubble_sort
import bucket_sort
import comb_sort
import count_sort
import heap_sort
import insertion_sort
import merge_sort
import quick_sort
import radix_sort
import selection_sort
import shell_sort

import unittest
from nose.tools import assert_raises


class TestSortingAlgorithm(object):

    def empty_input(self, fn):
        """Test function can handle empty input
        """
        print fn
        assert(fn([]) == [])

    def single_element(self, fn):
        """Test function returns correct result for single element input
        """
        ls = [5]
        assert(fn(ls) == ls)

    def sort_sorted(self, fn):
        """Test sorting on a sorted list
        """
        ls = [-1, 0, 1, 2, 3]
        assert(fn(ls) == ls)

    def random(self, fn):
        """Test sorting result is correct
        """
        ls = [5, 2, 6, 8, 0, 4, -2, -1]
        assert(fn(ls) == sorted(ls))

    def tuple_compatiable(self, fn):
        """Test function handles tuple input
        """
        tp = (0, 4, -3, 6, 20, 40.0)
        assert_raises(TypeError, fn, tp)

    def string_compatiable(self, fn):
        """Test function handles string input
        """
        s = r"082389hqwehfy\aoweFE$GH%TW#%TSDGSf"
        assert_raises(TypeError, fn, s)

    def test_all(self):
        """Run all tests on each sorting algorithm
        """
        for fn in (bubble_sort.sort, insertion_sort.sort):
            yield self.empty_input, fn
            yield self.single_element, fn
            yield self.sort_sorted, fn
            yield self.random, fn
            yield self.tuple_compatiable, fn
            yield self.string_compatiable, fn


if __name__ == '__main__':
    unittest.main()
