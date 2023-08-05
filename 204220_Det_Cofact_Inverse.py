# This function returns the transpose of a matrix
def transposeMatrix(m):
    transpose=list(map(list,zip(*m)))
    return transpose


# This function returns the minor matrix of the element
# at postion i,j
def getMatrixMinor(m,i,j):
    minor_matrix = [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]
    return minor_matrix



# This function find the determinant of the matrix
def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant




def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    if(determinant==0):
        print('Error! Determinant of the matrix is zero')
        print('Inverse cannot be calculated')
        return
    
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]
    
    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
        
    # Transposing the cofactor matrix to get disjoint
    Disjoint = transposeMatrix(cofactors)
    
    # Dividing each element of the adjoint matrix by the determinant
    for r in range(len(Disjoint)):
        for c in range(len(Disjoint)):
            Disjoint[r][c] = Disjoint[r][c]/determinant
            
    return Disjoint


#matrix A 
print("Enter the dimension of the matrix")
row1 = int(input("Row = "))
col1 = int(input("Colunm = "))

mat1= []
print("Enter the matrix elements")
for x in range(row1):
    list1= []
    for i in range(col1):
        print(x," row ",i," element")
        a = int(input())
        list1.append(a)
    mat1.append(list1)


#printing the matrix
#matrix A
print("Matrix A",mat1)

#printing the inverse matrix
print("inverse",getMatrixInverse(mat1))


