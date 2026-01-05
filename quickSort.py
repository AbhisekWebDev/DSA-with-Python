class Solution:

    # partition function
    def partition(self, arr, left, right):
        
        # choose the pivot
        pivot = arr[right]
        
        # index of smaller element and indicates 
        # the right position of pivot found so far
        i = left - 1
        
        # traverse arr[low..high] and move all smaller
        # elements to the left side. Elements from low to 
        # i are smaller after every iteration
        for j in range(left, right):
            if arr[j] < pivot:
                i += 1
                self.swap(arr, i, j)
        
        # move pivot after smaller elements and
        # return its position
        self.swap(arr, i + 1, right)
        
        return i + 1

    # swap function
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
    
    def quickSort(self, arr, left, right):

        if left < right:
            
            # pi is the partition return index of pivot
            pi = self.partition(arr, left, right)

            # recursion calls for smaller elements
            # and greater or equals elements
            self.quickSort(arr, left, pi - 1)
            self.quickSort(arr, pi + 1, right)

    def sortArray(self, nums) :

        # merge sort
        self.quickSort(nums, 0, len(nums) - 1)

        return nums

nums = [5,2,3,1]   

sol = Solution()
ans = sol.sortArray(nums)
print(ans)

# space complexity = O(1)
# time complexity = O(nlogn) [avg]
