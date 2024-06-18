class ShellSort:
    def sort(self, arr, attribute=None, reverse=False):
        n = len(arr)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and self.compare(arr[j - gap], temp, attribute, reverse):
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2
        return arr

    def sort_primitive_ascendent(self, arr):
        return self.sort(arr)

    def sort_primitive_descendent(self, arr):
        return self.sort(arr, reverse=True)

    def sort_models_ascendent(self, arr, attribute):
        return self.sort(arr, attribute)

    def sort_models_descendent(self, arr, attribute):
        return self.sort(arr, attribute, reverse=True)

    def compare(self, a, b, attribute=None, reverse=False):
        if attribute:
            if reverse:
                return getattr(a, attribute) < getattr(b, attribute)
            else:
                return getattr(a, attribute) > getattr(b, attribute)
        else:
            if reverse:
                return a < b
            else:
                return a > b