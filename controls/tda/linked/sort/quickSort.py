import random

class QuickSort:
    def sort(self, array, attribute=None, reverse=False):
        if len(array) <= 1:
            return array
        else:
            pivot = array[len(array) // 2] # random.randint(0, len(array) - 1)
            less, equal, greater = self.partition(array, pivot, attribute)
            if reverse:
                return self.sort(greater, attribute, reverse) + equal + self.sort(less, attribute, reverse)
            else:
                return self.sort(less, attribute, reverse) + equal + self.sort(greater, attribute, reverse)

    def sort_primitive_ascendent(self, array):
        return self.sort(array)

    def sort_primitive_descendent(self, array):
        return self.sort(array, reverse=True)

    def sort_models_ascendent(self, array, attribute):
        return self.sort(array, attribute)

    def sort_models_descendent(self, array, attribute):
        return self.sort(array, attribute, reverse=True)

    def partition(self, array, pivot, attribute=None):
        def compare(a, b):
            if attribute:
                return getattr(a, attribute) < getattr(b, attribute), getattr(a, attribute) == getattr(b, attribute)
            else:
                return a < b, a == b

        less, equal, greater = [], [], []
        for i in array:
            is_less, is_equal = compare(i, pivot)
            if is_less:
                less.append(i)
            elif is_equal:
                equal.append(i)
            else:
                greater.append(i)
        return less, equal, greater