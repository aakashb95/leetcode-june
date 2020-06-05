class Solution:
    def __init__(self, w: List[int]):
        self.arr = w
        self.n = len(w)

        for i in range(1, self.n):
            self.arr[i] += self.arr[i - 1]

        self.accumulated_sum = self.arr[-1]

    def pickIndex(self) -> int:
        seed = random.randint(1, self.accumulated_sum)
        return self.binary_search(self.arr, seed)

    def binary_search(self, arr, target):
        i, j = 0, len(arr) - 1
        while i <= j:
            mid = (i + j) // 2
            if target > arr[mid]:
                i = mid + 1
            elif target == arr[mid]:
                return mid
            else:
                j = mid - 1
        if i > j:
            return i
