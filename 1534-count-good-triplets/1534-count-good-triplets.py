class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        triplets = []
        for i in range(len(arr)):
            for j in range(len(arr)):
                for k in range(len(arr)):
                    if 0 <= i < j < k < len(arr):
                        if abs(arr[i] - arr[j]) <= a:
                            if abs(arr[j] - arr[k]) <= b:
                                if abs(arr[i] - arr[k]) <= c:
                                    triplets.append([arr[i], arr[j], arr[k]])
        return len(triplets)