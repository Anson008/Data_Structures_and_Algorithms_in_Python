def binary_sum(S, start, stop):
    """Return the sum of the number in implicit slice S[start: stop]."""
    if start >= stop:
        return 0
    elif start == stop - 1:
        return S[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)


if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5]
    print(binary_sum(l1, 0, len(l1)))
