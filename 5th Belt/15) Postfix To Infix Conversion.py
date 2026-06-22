# Postfix to Infix Conversion
# Convert a postfix expression into its equivalent
# infix expression using a stack.
#
# The resulting infix expression must be enclosed
# in parentheses to clearly denote precedence.

def is_operator(token):
    return token in "+-*/^"

def postfix_to_infix(postfix):
    stack = []

    for token in postfix.split():
        if is_operator(token):
            b = stack.pop()
            a = stack.pop()
            stack.append(f"({a} {token} {b})")
        else:
            stack.append(token)

    return stack[-1]

if __name__ == "__main__":
    postfix = input().strip()
    infix = postfix_to_infix(postfix)
    print(infix)