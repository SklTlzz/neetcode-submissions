class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": lambda x, y: x + y, 
            "-": lambda x, y: x - y, 
            "*": lambda x, y: x * y, 
            "/": lambda x, y: x / y
        }

        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                last_val = stack.pop()
                pre_last_val = stack.pop()

                result = int(ops[token](pre_last_val, last_val))

                stack.append(result)

        return stack[0]
