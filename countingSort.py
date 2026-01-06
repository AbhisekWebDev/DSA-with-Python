# this algo is used when the array has a limit
# for ex: arr = [0 to 100], [1 to 10], ...

class Solution:

    def sortArray(self, nums) :

        mx = max(nums) + 1

        # ab ek frequency array lenge 
        # aur size mx+1 how aur initially array me 0 fill krenge 
        # aur jiska jitna frequency hoga usko isme store krte rhenge
        freq = [0] * mx

        for i in nums :
            # freq++
            freq[i] += 1

        # nums array ko empty kro
        nums = []

        for i in range(0, mx) :

            while freq[i] > 0 :
                nums.append(i)
                # freq--
                freq[i] -= 1

        return nums

nums = [5,2,3,1]   

sol = Solution()
ans = sol.sortArray(nums)
print(ans)

# space complexity = O(mx)
# time complexity = O(n) for all cases