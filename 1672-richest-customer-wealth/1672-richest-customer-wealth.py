class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        highest = 0
        for i in range(len(accounts)):
            if sum(accounts[i]) > highest:
                highest = sum(accounts[i])
        return highest