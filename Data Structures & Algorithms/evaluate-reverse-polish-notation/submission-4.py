_OPERATORS = {'+', '-', '*', '/'}



class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        eval_stack: list[str | int] = list()

        for curr in tokens:
            if curr in _OPERATORS:
                operand_1 = int(eval_stack.pop())
                operand_0 = int(eval_stack.pop())
                if curr == "+":
                    eval_stack.append(operand_0 + operand_1)
                elif curr =="-":
                    eval_stack.append(operand_0 - operand_1)
                elif curr =="*":
                    eval_stack.append(operand_0 * operand_1)
                else:
                    eval_stack.append(int(operand_0 / operand_1))

            else:
                eval_stack.append(curr)
        
        return int(eval_stack[0])