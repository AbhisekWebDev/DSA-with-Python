class Solution:

    # using Hoare's Partition Algorithm

    # Function to partition the array according to pivot index element
    def partition(self, arr, left, right):
        pivot = arr[left]
        
        i = left - 1
        j = right + 1
        
        while True:
        
            # find next element larger than pivot from the left
            while True:
                i += 1
                if arr[i] >= pivot:
                    break
            
            # find next element smaller than pivot from the right
            while True:
                j -= 1
                if arr[j] <= pivot:
                    break
            
            # if left and right crosses each other no swapping required
            if i >= j:
                return j
            
            # swap larger and smaller elements
            arr[i], arr[j] = arr[j], arr[i]

    # swap function
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
    
    def quickSort(self, arr, left, right):

        if left < right:
            
            # pi is the partition return index of pivot
            pi = self.partition(arr, left, right)

            # recursion calls for smaller elements
            # and greater or equals elements
            self.quickSort(arr, left, pi)
            self.quickSort(arr, pi + 1, right)

    def sortArray(self, nums) :

        # merge sort
        self.quickSort(nums, 0, len(nums) - 1)

        return nums

nums = [5,2,3,1]   

sol = Solution()
ans = sol.sortArray(nums)
print(ans)


# For Hoare Partition, the partition function returns j
# not the pivot index

# So recursion MUST be:

# (left , j)
# (j+1 , right)