# Intuition:
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        d = {}
        for i, n in enumerate(citations, 1):
            d[i] = n

        h = []
        for k, v in d.items():
            if d[k] >= k:
                h.append(k)

        return max(h) if h else 0


# O(logn) solution --> Not fully understood
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        i = 0
        j = len(citations) - 1
        while i <= j:
            mid = i + (j - i) // 2
            if citations[mid] >= len(citations) - mid:
                j = mid - 1
            else:
                i = mid + 1
        return len(citations) - i

