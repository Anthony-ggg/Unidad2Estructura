class MergeSort:
    def sort(self, array, attribute=None, reverse=False):
        buffer = [0] * len(array)
        self.merge_sort(array, 0, len(array) - 1, buffer, attribute)
        return array[::-1] if reverse else array

    def sort_primitive_ascendent(self, nums):
        return self.sort(nums)

    def sort_primitive_descendent(self, nums):
        return self.sort(nums, reverse=True)

    def sort_models_ascendent(self, array, attribute):
        return self.sort(array, attribute)

    def sort_models_descendent(self, array, attribute):
        return self.sort(array, attribute, reverse=True)

    def merge_sort(self, nums, start, last, buffer, attribute=None):
        if start < last:
            mid = (start + last) // 2
            self.merge_sort(nums, start, mid, buffer, attribute)
            self.merge_sort(nums, mid + 1, last, buffer, attribute)
            self.merge_two_array(nums, start, mid, last, buffer, attribute)

    def merge_two_array(self, nums, start, mid, last, buffer, attribute=None):
        def compare(a, b):
            if attribute:
                return getattr(a, attribute) <= getattr(b, attribute)
            else:
                return a <= b

        left = start
        right = mid + 1
        i = left
        while left <= mid and right <= last:
            if compare(nums[left], nums[right]):
                buffer[i] = nums[left]
                left += 1
            else:
                buffer[i] = nums[right]
                right += 1
            i += 1

        while left <= mid:
            buffer[i] = nums[left]
            left += 1
            i += 1

        while right <= last:
            buffer[i] = nums[right]
            right += 1
            i += 1

        for j in range(start, last + 1):
            nums[j] = buffer[j]