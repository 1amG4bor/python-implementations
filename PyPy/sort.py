# Merge sort algorithm


def __sorting(data):
    """
    Custom recursive implementation of merge sort algorithm
    NOT OPTIMIZED FOR PERFORMANCE
    """
    # divide list
    if len(data) < 2:
        return data
    else:
        mid = int(len(data) / 2)
        left = __sorting(data[:mid])
        right = __sorting(data[mid:])

    # merge chunks
    sorted = []
    while left or right:
        if not left:
            sorted.append(right.pop(0))
        elif not right:
            sorted.append(left.pop(0))
        else:
            sorted.append(left.pop(0) if left[0] < right[0] else right.pop(0))
    return sorted


def merge_sort(data, display_result=True):
    result = __sorting(data[:])
    if display_result:
        print("Sorted numbers (merge-sort):\t", result)
    return result
