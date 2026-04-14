class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = sorted(list(zip(position,speed)), key=lambda x: x[0], reverse=True)
        stack=[]
        for x,y in combined:
            time = (target-x)/y
            if not stack or stack[-1]<time:
                stack.append(time)
        return len(stack)


