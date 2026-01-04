def maxProdSubarray(nums) :

    max_here = nums[0]
    min_here = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        n = nums[i]

        if n < 0:
            max_here, min_here = min_here, max_here

        prev_max = max_here
        prev_min = min_here

        max_here = max(n, prev_max * n)
        min_here = min(n, prev_min * n)

        result = max(result, max_here)

    return result

nums = [1,5,9,7,-8,3,4,6,2,8,0,-1,-5,-7]

print(maxProdSubarray(nums))