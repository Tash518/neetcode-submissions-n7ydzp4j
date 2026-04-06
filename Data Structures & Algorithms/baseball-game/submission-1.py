class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record =[]
        for c in operations:
            if c.lstrip('-').isdigit():
                record.append(int(c))
            if c=="+":
                record.append(record[-1]+record[-2])
            if c=="D":
                record.append(2*record[-1])
            if c=="C":
                record.pop()
        return sum(record)