from Chapter_06.Examples_C06.stack import ArrayStack


def is_matched(expr):
    """Return True if all delimiters are properly matched; False otherwise."""
    lefty = '({['
    righty = ')}]'
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()


if __name__ == "__main__":
    expr1 = "(({}))[]"
    print(is_matched(expr1))
