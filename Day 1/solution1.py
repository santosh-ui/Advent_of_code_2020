from typing import List, Optional

def exists_binary_search(
    array: List[int],
    value: int,
    start: Optional[int] = None,
    end: Optional[int] = None
           ) -> bool:
    if start is None or end is None:
        start, end = 0, len(array)-1

    if start > end:
        return False

    mid = (start + end) // 2

    if array[mid] == value:
        return True

    if array[mid] < value:
        return exists_binary_search(array, value, mid+1, end)

    return exists_binary_search(array, value, start, mid-1)


def part1() -> None:
    with open("input.txt") as infile:
        nums = [int(line) for line in infile.readlines()]

    nums.sort()

    for num in nums:
        complement = 2020 - num
        exists = exists_binary_search(nums, complement)
        if exists:
            print(num * complement)
            return

part1()
