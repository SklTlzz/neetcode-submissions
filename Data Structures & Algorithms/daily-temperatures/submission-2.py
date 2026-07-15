class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack_of_idxs = []

        for i in range(len(temperatures)):
            while stack_of_idxs and temperatures[i] > temperatures[stack_of_idxs[-1]]:
                result[stack_of_idxs[-1]] = i - stack_of_idxs[-1]
                stack_of_idxs.pop()

            stack_of_idxs.append(i)

        return result            
