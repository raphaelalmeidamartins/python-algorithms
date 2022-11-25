from collections import Counter


def find_duplicate(nums):
    if type(nums) is not list or all(
        [
            type(num) is not int or num < 1
            for num in nums
        ]
    ):
        return False

    num, count = Counter(nums).most_common()[0]

    if count > 1:
        return num

    return False
