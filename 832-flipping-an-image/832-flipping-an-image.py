class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for arr in image:
            arr.reverse()
            for i in range(len(arr)):
                arr[i] = arr[i]^1
        return image