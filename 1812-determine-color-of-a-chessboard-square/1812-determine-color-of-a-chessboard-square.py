class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
    
        """
        if (ord(coordinates[0]) - 96) % 2 != 0 and int(coordinates[1]) % 2 != 0:
            return False
        if (ord(coordinates[0]) - 96) % 2 == 0 and int(coordinates[1]) % 2 == 0:
            return False
        return True
            