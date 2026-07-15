class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack_of_idxs = []

        for i in range(len(temperatures)):
            if not stack_of_idxs:
                stack_of_idxs.append(i)
            else:
                while temperatures[i] > temperatures[stack_of_idxs[-1] if stack_of_idxs else i]:
                    result[stack_of_idxs[-1]] = i - stack_of_idxs[-1]
                    stack_of_idxs.pop()

                stack_of_idxs.append(i)

        return result            
