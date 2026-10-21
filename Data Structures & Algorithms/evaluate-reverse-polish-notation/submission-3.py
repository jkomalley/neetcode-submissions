class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            # print(f"{tok=} {stack=}")
            if tok.isnumeric() or tok[1:].isnumeric():
                stack.append(int(tok))
            elif tok == "+":
                stack = stack + [stack.pop() + stack.pop()]
            elif tok == "-":
                stack = stack + [-stack.pop() + stack.pop()]
            elif tok == "*":
                stack = stack + [stack.pop() * stack.pop()]
            elif tok == "/":
                b = stack.pop()
                a = stack.pop()

                c = a / b

                if c < 0:
                    c = math.ceil(c)
                else:
                    c = math.floor(c)
                
                stack = stack + [c]
        
        return stack.pop()