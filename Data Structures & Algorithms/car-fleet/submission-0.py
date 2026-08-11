class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        fleet = 0

        for position, speed in cars:
            time = (target - position) / speed
            stack.append(time)

            while len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
