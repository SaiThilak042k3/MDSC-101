def inputEq():
	unknown= int(input('Number of unknown : '))

	unknownsCoff=[]
	for i in range(1,unknown+1):
		list1= []
		for j in range(1,unknown+2):
			if(j == unknown+1):
				print(i," Eqution's Constant element")
			else:
				print(i," Eqution's ",j," unknown's Coefficient")
			a = int(input())
			list1.append(a)
		unknownsCoff.append(list1)

	return unknownsCoff
        
#____________________________________

def printequations(mat):
	for i in mat:
		print(i)

#____________________________________

def GE(matrix):
	for i in range(len(matrix)):
		for k in range(i+1, len(matrix)):
			temp = matrix[k][i]
			matrix[k][i] = matrix[k][i] - ((matrix[k][i]*matrix[i][i])/matrix[i][i])
			if(k == i+1):
				for j in range(len(matrix)+1):
					matrix[k][j] = matrix[k][j] - ((matrix[k][j]*temp)/temp)			
	return matrix

#____________________________________

def solEQ(mat):
	if(mat[len(mat)-1] == 0):
		print("Infinitly Many Solutions")
	else:
		for i in range(mat)

	for i in range(len(mat)-1):
		mat[len(mat)-1] 

#____________________________________

mat = inputEq()

print("Input Matrix")
printequations(mat)

print("Row Echolean Matrix")
gaussMat = GE(mat)
printequations(gaussMat)
#solEQ(gaussMat)