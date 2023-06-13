# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.


def overlap(a_min, a_max, b_min, b_max):
    return not (b_min > a_max or a_min > b_max)

def rooms(times):
    max_overlaps = 0
    for i in range(len(times)):
        overlaps = 1 #overlap with self
        for j in range(i):
            start, end = times[i]
            cmp_start, cmp_end = times[j]
            if overlap(start, end, cmp_start, cmp_end):
                overlaps += 1
        max_overlaps = max(max_overlaps, overlaps)
    return max_overlaps

print(rooms([(30, 75), (0, 50), (60, 150)])) #=> 2