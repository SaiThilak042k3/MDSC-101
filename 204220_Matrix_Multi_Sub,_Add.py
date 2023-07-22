#matrix add, sub, mul


#ADDITION
def addition():
    
    final_matrix2= []
    for x in range(row1):
        final_matrix1= []
        for i in range(col1):
            final_matrix1.append(int(list2[x][i]) + int(list4[x][i]))
        final_matrix2.append(final_matrix1)

    #printing the matrix 
    for x in range(row1):
        print(final_matrix2[x],"\n")

#SUBRACTION
def subraction():
    
    final_matrix2= []
    for x in range(row1):
        final_matrix1= []
        for i in range(col1):
            final_matrix1.append(int(list2[x][i]) - int(list4[x][i]))
        final_matrix2.append(final_matrix1)

    #printing the matrix
    for x in range(row1):
        print(final_matrix2[x],"\n")



#MULTIPLICATION
def multiplication():
    final_matrix2= []
    for x in range(row1):
        final_matrix1= []
        for i in range(col2):
            a= 0
            for n in range(col1):
                a += (int(list2[x][n]) * int(list4[n][i]))
            final_matrix1.append(a)
        final_matrix2.append(final_matrix1)

    #printing the matrix
    for x in range(row1):
        print(final_matrix2[x],"\n")
            

#inputs

#matrix A
print("Enter the dimension of the A matrix")
row1 = int(input("Row = "))
col1 = int(input("Colunm = "))

list2= []
print("Enter the A matrix elements")
for x in range(row1):
    list1= []
    for i in range(col1):
        print(x," row ",i," element")
        a = input()
        list1.append(a)
    list2.append(list1)

#matrix B
print("Enter the dimension of the B matrix")
row2 = int(input("Row = "))
col2 = int(input("Colunm = "))
list4= []
print("Enter the B matrix elements")
for x in range(row2):
    list3= []
    for i in range(col2):
        print(x," row ",i," element")
        a = input()
        list3.append(a)
    list4.append(list3)



#printing the matrix
#matrix A
for x in range(int(row1)):
    print(list2[x],"\n")
#matrix B
for x in range(int(row2)):
    print(list4[x],"\n")

    
#operations
choose = int(input("\n1. Addtion\n2. Subraction\n3. Multiplication\nEnter the operation: "))

if(choose == 1):
    if(row1 == row2 and col1 == col2):
        addition()
    else:
        print("row and co1 should be same!")
    
elif(choose == 2):
    if(row1 == row2 and col1 == col2):
        subraction()
    else:
        print("row and co1 should be same!")
elif(choose == 3):
    if(col1 == row2):
        multiplication()
    else:
        print("row and co1 should be same!")
else:
    print("Input is worng!\n")


print("END of the Program!!!")

