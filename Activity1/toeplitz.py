# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
# 
# Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
# 
# 
# Example 1:
# 
# Input:
# matrix = [
#   [1,2,3,4],
#   [5,1,2,3],
#   [9,5,1,2]
# ]
# Output: True
# Explanation:
# In the above grid, the diagonals are:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
# In each diagonal all elements are the same, so the answer is True.
# Example 2:
# 
# Input:
# matrix = [
#   [1,2],
#   [2,2]
# ]
# Output: False
# Explanation:
# The diagonal "[1, 2]" has different elements.
# 
# Note:
# 
# matrix will be a 2D array of integers.
# matrix will have a number of rows and columns in range [1, 20].
# matrix[i][j] will be integers in range [0, 99].

class Solution:
        def isToeplitzMatrix(self, matrix: 'List[List[int]]') -> 'bool':

                for i in range(len(matrix)):
                    f = (len(matrix)-1)-i
                    array = []
                    for j in range(i+1):
                        array.append(matrix[j][f+j])
                        if j == (len(matrix[0])-1):
                            pass

                    for k in range(1,len(array)):
                        if array[k] == array[(k-1)]:
                            continue
                        else:
                            return False



                for i in range(len(matrix[0])):
                    f = (len(matrix[0])-1)-i
                    array = []
                    
                    for j in range(i+1):
                        array.append(matrix[f+j][j])
                        if j == (len(matrix)-1):
                            pass
                    for k in range(1,len(array)):
                        if array[k] == array[(k-1)]:
                            continue
                        else:
                            return False
                pass

