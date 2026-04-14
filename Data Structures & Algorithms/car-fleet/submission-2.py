class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = list(zip(position,speed))
        combined.sort(key=lambda x: x[0], reverse=True)
        times = []
        for x,y in combined:
            times.append((target-x)/y)
        stack=[]
        print(times)
        for i in range(len(times)):
            if not stack or times[stack[-1]]<times[i]:
                stack.append(i)

        print(len(stack))
        return len(stack)


