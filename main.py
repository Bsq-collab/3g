from display import *
from draw import *
from matrix import *


screen = new_screen()
color = [ 0, 255, 255 ]
matrix = new_matrix()
print "TESTING PRINT MATRIX"
print_matrix(matrix)
print "TESTING IDENTITY MATRIX"
ident(matrix)
print_matrix(matrix)
print "MULTIPLYING MATRICES"
# 4x4 matrix
X = [[12,7,3,6],
    [4 ,5,6,6],
    [7 ,8,9,6],
    [3,4,5,6]]
# 4xN matrix
Y = [[5,8,1,2,10],
    [6,7,3,0,10],
    [4,5,9,1,10],
    [1,2,3,4,5]]
'''
EXPETED:
[120, 172, 78, 51, 250]
[80, 109, 91, 38, 180]
[125, 169, 130, 47, 270]
[65, 89, 78, 35, 150]
'''
matrix_mult(X,Y)

matrix = [[100, 400, 400, 400],
          [100, 400, 400, 400],
          [10, 10, 100, 0],
          [0, 0, 0, 0]]

for x in range(10, 500):
    add_edge(matrix, 250, 250, 0, x, 400, 0)
draw_lines( matrix, screen, color )


display(screen)
