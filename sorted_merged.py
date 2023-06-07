# return a new sorted merged list from K sorted lists, each with size N

def test(solution):
    cases = [
        [],
        [[],[],[]],
        [[],[1],[1,2]],
        [[1]],
        [[1],[1,3,5],[1,10,20,30,40]]
    ]
    answers = [
        [],
        [],
        [1,1,2],
        [1],
        [1,1,1,3,5,10,20,30,40]
    ]
    for case, answer in zip(cases, answers):
        result = solution(case)
        if result != answer:
            raise ValueError(f'Case {case}: Expected {answer}, got {result} for "{solution.__name__}" solution')
    print(f'"{solution.__name__}" solution passed {len(cases)} tests')


def naive(arrs):
    merged = []
    for arr in arrs:
        for x in arr:
            merged.append(x)
    return sorted(merged)


def merge(l_arr, r_arr):
    l_i = 0
    r_i = 0
    merged = []
    while l_i < len(l_arr) and r_i < len(r_arr):
        left = l_arr[l_i]
        right = r_arr[r_i]
        if left < right:
            merged.append(left)
            l_i += 1
        else:
            merged.append(right)
            r_i += 1
    return merged + l_arr[l_i:] + r_arr[r_i:]

def recursive(arrs):
    count = len(arrs)
    if count == 0:
        # no elements
        return []
    elif count == 1:
        # nothing to merge
        return arrs[0]
    elif count == 2:
        # merge two arrays
        return merge(arrs[0], arrs[1])
    else:
        # recursively merge arrays
        mid = count // 2
        return merge(recursive(arrs[:mid]), recursive(arrs[mid:]))


test(naive)
test(recursive)
