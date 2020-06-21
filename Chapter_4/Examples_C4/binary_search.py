def binary_search(data, target, low, high):
    """
    Return True if target is found in indicated portion of a Python list.
    The search only considers the portion from data[low] to data[high] inclusive.
    
    :param data: list. A sorted Python list of int, float or str
    :param target: int, float, or str. The target to search in the sorted list.
    :param low: int. Index of the lower boundary of the searching interval.
    :param high: int. Index of the upper boundary of the searching interval.
    :return: boolean. True if the target is found; otherwise, False.
    """
    if low > high:  # interval is empty, no match
        return False  
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            # Recur on the portion left of the middle.
            return binary_search(data, target, low, mid - 1)
        else:
            # Recur on the portion right of the middle.
            return binary_search(data, target, mid + 1, high)
        

if __name__ == "__main__":
    data1 = [1, 2, 5, 7, 12, 35]
    target1 = 5
    res1 = binary_search(data1, target1, 0, len(data1))
    print(f'{target1} in {data1}? -- {res1}')
    
    data2 = [0.1, 4.2, 5.9, 7.7, 12.3, 17.1]
    target2 = 0.1
    res2 = binary_search(data2, target2, 0, len(data2))
    print(f'{target2} in {data2}? -- {res2}')
    
    data3 = ['a', 'b', 'c', 'e', 'i', 'l', 'x']
    target3 = 'x'
    res3 = binary_search(data3, target3, 0, len(data3))
    print(f'{target3} in {data3}? -- {res3}')
