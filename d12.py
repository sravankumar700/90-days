
"""
Array Practice Questions (3 levels: Beginner -> Advanced)

1) Beginner: Two Sum (Indices)
	 Description:
		 Given an array of integers nums and a target integer, return the indices
		 of the two numbers such that they add up to target. Assume exactly one
		 solution exists and you may not use the same element twice.
	 Example:
		 nums = [2,7,11,15], target = 9 -> output: [0,1]
	 Constraints:
		 - 2 <= len(nums) <= 1e5, values fit in 32-bit int
	 Hint: Use a hash map to store seen values to get O(n) time.

2) Intermediate: Longest Subarray With Sum K
	 Description:
		 Given an array of integers (can include negative numbers) and integer K,
		 return the length of the longest contiguous subarray whose sum equals K.
		 If none exists, return 0.
	 Example:
		 nums = [1, -1, 5, -2, 3], K = 3 -> output: 4  (subarray [1, -1, 5, -2])
	 Constraints:
		 - len(nums) <= 2e5, values maybe negative
	 Hint: Use prefix sums and a hash map to record earliest index of each prefix sum.

3) Advanced: Minimum Window to Sort (or Minimum Swaps to Sort Subarray)
	 Description:
		 Given an array of integers, find the length of the shortest contiguous
		 subarray that, if sorted in non-decreasing order, makes the whole array
		 sorted. Return 0 if the array is already sorted.
	 Example:
		 nums = [2,6,4,8,10,9,15] -> output: 5 (subarray [6,4,8,10,9])
	 Constraints:
		 - len(nums) <= 1e5
	 Hint: Compute prefix max from left and prefix min from right (or compare with sorted copy)

"""

if __name__ == '__main__':
		# Placeholder: print the three problem titles
		print("1) Two Sum (Indices)")
		print("2) Longest Subarray With Sum K")
		print("3) Minimum Window to Sort")
