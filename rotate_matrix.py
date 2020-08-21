
def print_matrix(matrix):
    for row in matrix:
        print(row)
    return None

def rotate_matrix(matrix):

    """
    Assume a matrix of the form [[1, 2, 3],
                                 [2, 2, 3],
                                 [3, 2, 2]]
    """

    width = len(matrix[0])
    length = len(matrix)
    offset = -1

    result_matrix = []
    
    for i in range(width):
        new_row = []
        for j in range(length):
            print(length-j-1)
            new_row.append(matrix[length - j - 1][i])
        result_matrix.append(new_row)

    return result_matrix

M = [[1, 2, 3],
     [1, 2, 3],
     [1, 2, 3]]

print_matrix(rotate_matrix(M))

# Python3 program to rotate a matrix by 90 degrees 
N = 3

# An Inplace function to rotate 
# N x N matrix by 90 degrees in 
# anti-clockwise direction 
def rotateMatrix(mat): 
	
	# Consider all squares one by one 
	for x in range(0, int(N / 2)): 
		
		# Consider elements in group 
		# of 4 in current square 
		for y in range(x, N-x-1): 
			
			# store current cell in temp variable 
			temp = mat[x][y] 

			# move values from right to top 
			mat[x][y] = mat[y][N-1-x] 

			# move values from bottom to right 
			mat[y][N-1-x] = mat[N-1-x][N-1-y] 

			# move values from left to bottom 
			mat[N-1-x][N-1-y] = mat[N-1-y][x] 

			# assign temp to left 
			mat[N-1-y][x] = temp 


# Function to print the matrix 
def displayMatrix( mat ): 
	
	for i in range(0, N): 
		
		for j in range(0, N): 
			
			print (mat[i][j], end = ' ') 
		print ("") 
	
	


# Driver Code 
mat = [[0 for x in range(N)] for y in range(N)] 

# Test case 1 
mat = [ [1, 2, 3], 
		[5, 6, 7], 
		[9, 10, 11], 
		[13, 14, 15] ] 
		
''' 
# Test case 2 
mat = [ [1, 2, 3 ], 
		[4, 5, 6 ], 
		[7, 8, 9 ] ] 

# Test case 3 
mat = [ [1, 2 ], 
		[4, 5 ] ] 
		
'''

rotateMatrix(mat) 

# Print rotated matrix 
displayMatrix(mat) 


# This code is contributed by saloni1297 

