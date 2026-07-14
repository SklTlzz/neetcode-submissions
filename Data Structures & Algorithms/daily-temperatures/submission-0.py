class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        flag = False

        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result.append(j - i)
                    flag = True
                    break

            if not flag:
                result.append(0)

            flag = False

        return result
