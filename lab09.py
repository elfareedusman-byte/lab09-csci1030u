# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline:
    # Keep a dictionary mapping each number we've seen so far to its index.
    # As we loop through nums, calculate the complement (target - num).
    # If the complement is already in the dictionary, return [seen[complement], i].
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


def max_profit(prices):
    # Outline:
    # Track the lowest stock price seen so far and the maximum profit found.
    # For each day's price, update the minimum price if it's lower, or check if
    # selling today beats our best profit so far.
    min_price = float("inf")
    best_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > best_profit:
            best_profit = price - min_price
    return best_profit


def max_subarray(nums):
    # Outline:
    # Track the running sum of the current contiguous subarray and the overall max sum.
    # At each number, decide whether to extend the current subarray or start fresh
    # at the current number, then update the overall best sum.
    current_sum = nums[0]
    best_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        best_sum = max(best_sum, current_sum)
    return best_sum


def is_balanced(s):
    # Outline:
    # Use a list as a stack to push opening brackets.
    # When a closing bracket appears, pop the top of the stack and verify it matches.
    # At the end, return True only if the stack is completely empty.
    stack = []
    matching = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in matching:
            if not stack or stack.pop() != matching[ch]:
                return False
    return len(stack) == 0


if __name__ == "__main__":
    main()
