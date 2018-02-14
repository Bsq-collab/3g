import math


def print_matrix( matrix ):
    print matrix;
    pass

def ident( matrix ):
    for row in range(4):
        for col in range(4):
            if row=col:
                matrix[row][col]=1
            else:
                matrix[row][col]=0
    return matrix
        

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    pass




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
