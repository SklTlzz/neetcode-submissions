class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        count_fleets = 0
        cars = []
        stack = []

        for i in range(len(position)):
            cars.append((position[i], speed[i]))

        cars = sorted(cars, reverse=True)

        for car in cars:
            pos, speed = car
            hours_to_dest = (target - pos) / speed

            if hours_to_dest > (stack[-1] if stack else 0):
                stack.append(hours_to_dest)

        return len(stack)
