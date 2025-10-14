class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        def execute_stack(stack):

            a = int(stack[-3])
            b = int(stack[-2])
            op = stack[-1]

            del stack[-1]
            del stack[-1]
            del stack[-1]

            if op == "+":
                stack.append(a+b)
            elif op == "-":
                stack.append(a-b)
            elif op == "*":
                stack.append(a*b)
            elif op == "/":
                stack.append(a/b)

        def is_int(x):
            try:
                int(x)
                return True
            except ValueError:
                return False

        stack = []

        for token in tokens:

            stack.append(token)

            if not is_int(token):
                execute_stack(stack)
            

        while len(stack) >= 3:
            execute_stack(stack)
        
        return int(stack[0])

