class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        count = 0
        if ruleKey == "type":
            idx = 0
            for item in items:
                if item[idx] == ruleValue:
                    count += 1
        if ruleKey == "color":
            idx = 1
            for item in items:
                if item[idx] == ruleValue:
                    count += 1
        if ruleKey == "name":
            idx = 2
            for item in items:
                if item[idx] == ruleValue:
                    count += 1
        return count
                    
        
            