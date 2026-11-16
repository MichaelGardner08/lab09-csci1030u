# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline: I plan to run through the array using two loops, adding the first value of the array to every other individually,
    # and compare them to the target. Then, if no pair is found, I'll shift to the second value of the array and keep going until I find the working pair.
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):

            if nums[i] + nums[j] == target:
                return [i, j]
    


def max_profit(prices):
    # Outline: Similarly to two_sums, I'll use two loops to compare buying and selling prices, but only allow selling on a later day.
    # Additionally, i'll keep track of the highest profit so I know what the best day to sell is even when I 

    max_profit = 0

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):

            profit = prices[j] - prices[i]

            if profit > max_profit:
                max_profit = profit

    return max_profit


def max_subarray(nums):
    # Outline: Again, i'll be using two loops to find every possible contiguous block, keep track of the sum of each block,
    # and update max_sum whenever we find a larger sum.

    max_sum = nums[0]

    for i in range(len(nums)):
        current_sum = 0

        for j in range(i, len(nums)):
            current_sum += nums[j]

            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
