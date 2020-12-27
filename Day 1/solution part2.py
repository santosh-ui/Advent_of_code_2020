from typing import List, Optional

def exists_binary_search(
    array: List[int],
    value: int,
    start: Optional[int] = None,
    end: Optional[int] = None
    ) -> bool:
    if start is None and end is None:
        start, end = 0, len(array)-1

    if start > end:
        return False

    mid = (start + end) // 2

    if array[mid] == value:
        return True
    
    if array[mid] < start:
        return exists_binary_search(array, value, mid+1, end)
    return exists_binary_search(array, value, start, mid-1)


def part2() -> None:
    with open("input.txt") as infile:
        nums = [int(line) for line in infile]

    nums.sort()

    for i, num1 in enumerate(nums):
        for num2 in nums[i+1:]:
            complement = 2020 - (num1 + num2)
            exists = exists_binary_search(nums, complement)

            if exists:
                print(num1 * num2 * complement)
                return
            


part2()
