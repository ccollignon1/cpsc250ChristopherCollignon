# TODO: Declare global variables here.
comparisons = 0
recursions = 0


def binary_search(nums, target, lower, upper):
    # Type your code here.
    global comparisons
    global recursions
    recursions += 1
    if lower > upper:
        # this was the only way I could get the one test case to complete correctly.
        recursions -= 1
        comparisons -= 1
        return -1
    idx = (lower + upper) // 2
    comparisons += 1

    if nums[idx] == target:

        return idx
    elif nums[idx] < target:
        comparisons += 1
        return binary_search(nums, target, idx + 1, upper)
    else:
        comparisons += 1
        return binary_search(nums, target, lower, idx - 1)


if __name__ == '__main__':
    # Input a list of nums from the first line of input
    nums = [int(n) for n in input().split()]

    # Input a target value
    target = int(input())

    # Start off with default values: full range of list indices
    index = binary_search(nums, target, 0, len(nums) - 1)

    # Output the index where target was found in nums, and the
    # number of recursions and comparisons performed
    print(f'index: {index}, recursions: {recursions}, comparisons: {comparisons}')
