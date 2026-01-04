def KadanesAlgo(nums) :

    # kadane's algo

        curr_sum = 0

        max_sum = nums[0]

        for i in range(len(nums)) :

            curr_sum += nums[i]

            if curr_sum > max_sum :
                max_sum = curr_sum
            
            if curr_sum < 0 :
                curr_sum = 0
        
        return max_sum

nums = [1,5,9,7,-8,3,4,6,2,8,0,-1,-5,-7]

print(KadanesAlgo(nums))