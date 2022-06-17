class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        report = []
        for i in range(len(ops)):
            if ops[i] == "+":
                report.append(report[len(report) - 2] + report[len(report) -1])
            if ops[i] == "D":
                report.append(report[len(report) - 1] * 2)
            if ops[i] == "C":
                report.pop(len(report) - 1)
            if ops[i].isnumeric() or ops[i][0] == "-":
                report.append(int(ops[i]))
        return sum(report)