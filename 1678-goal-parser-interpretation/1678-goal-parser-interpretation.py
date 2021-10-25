class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        output = ""
        for i in range(len(command)):
            if command[i] == 'G':
                output += 'G'
            if command[i] == '(':
                if command[i + 1] == ')':
                    output += "o"
                else:
                    output += "al"
        return output
                    
                    
                    