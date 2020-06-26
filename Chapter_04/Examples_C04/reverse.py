def reverse(s, start, stop):
    """Reverse elements in implicit slice s[start:stop]."""
    if start < stop - 1:
        s[start], s[stop - 1] = s[stop - 1], s[start]
        reverse(s, start + 1, stop - 1)


if __name__ == "__main__":
    l1 = [1, 2, 3, 4]
    reverse(l1, 0, len(l1))
    print(l1)
