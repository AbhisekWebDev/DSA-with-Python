class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:

        # matrix la length
        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = (rows * cols) - 1

        while l <= r :

            mid = (l + r) // 2

            # cell ke coordinates nikalne ka tarika (formula)
                # matrix[mid // row] -> row number niklega
                # matrix[mid % col] -> col number niklega
            row = mid // cols
            col = mid % cols

            if matrix[row][col] == target :
                return True
            
            elif matrix[row][col] < target :

                # right
                l = mid + 1

            else : 

                # left 
                r = mid - 1
        
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

sol = Solution()
print(sol.searchMatrix(matrix, target))