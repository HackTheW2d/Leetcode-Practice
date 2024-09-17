
    

# def solution(mat):
#     m = len(mat)
#     n = len(mat[0])
#     visited = [[False for i in range(n)] for j in range(m)]
#     def border_check(i, j):
#         return i < m and j < n and i >= 0 and j >= 0
    
#     def traverse(i, j, dir):
#         x, y = dir
#         res = []
#         while border_check(i,j) and not visited[i][j]:
#             print(mat[i][j])
#             res.append(mat[i][j])
#             visited[i][j] = True
#             i += x
#             j += y
#         return res
    
    
#     def has_ways(i, j):
#         up = [i-1,j]
#         down = [i+1,j]
#         right = [i,j+1]
#         left = [i,j-1]
#         return (border_check(up[0], up[1]) and not visited[up[0]][up[1]]) or \
#             (border_check(down[0], down[1]) and not visited[down[0]][down[1]]) or \
#                 (border_check(left[0], left[1]) and not visited[left[0]][left[1]]) or \
#                     (border_check(right[0], right[1]) and not visited[right[0]][right[1]])
    
#     def spiral_traverse():
#         i, j = 0, 0
#         res = []
#         while has_ways(i,j):
#             res.append(traverse(i,j,(0,1)))
#             res.append(traverse(i,j,(1,0)))
#             res.append(traverse(i,j,(0,-1)))
#             res.append(traverse(i,j,(-1,0)))
        
#         return res
#     flattened = spiral_traverse()
#     return sum(x for idx, x in enumerate(flattened) if idx % 3 == 0 )

# print(solution([[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]))

# def spiral_order_sum(matrix):
#     if not matrix or not matrix[0]:
#         return 0

#     rows = len(matrix)
#     cols = len(matrix[0])
#     result = []

#     left, right, top, bottom = 0, cols - 1, 0, rows - 1

#     # Traverse the matrix in spiral order
#     while left <= right and top <= bottom:
#         # Traverse from left to right across the top row
#         for i in range(left, right + 1):
#             result.append(matrix[top][i])
#         top += 1

#         # Traverse from top to bottom down the right column
#         for i in range(top, bottom + 1):
#             result.append(matrix[i][right])
#         right -= 1

#         if top <= bottom:
#             # Traverse from right to left across the bottom row
#             for i in range(right, left - 1, -1):
#                 result.append(matrix[bottom][i])
#             bottom -= 1

#         if left <= right:
#             # Traverse from bottom to top up the left column
#             for i in range(bottom, top - 1, -1):
#                 result.append(matrix[i][left])
#             left += 1

#     # Now calculate the sum of elements at indices divisible by 3
#     total_sum = sum(result[i] for i in range(len(result)) if i % 3 == 0)

#     return total_sum

# # Example usage
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# result = spiral_order_sum(matrix)
# print(result)  # Output: 14
