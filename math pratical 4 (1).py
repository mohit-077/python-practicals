import numpy as np

# Taking input for coefficient Matrix (A)
print("Enter the dimensions of the cofficients matrix (A):")
NR = int(input("Enter the no of rows:"))
NC= int(input("Enter the no  of coloums:"))

#Taking input for the element of matrix A
print("Enter the element of the coefficient matrix (A) in a single line(seperated by space):")
Coefficient_Entries = list(map(float, input().split()))
Coefficient_Matrix = np.array(Coefficient_Entries).reshape(NR,NC)
print("Coefficients Matrix (A) is as follows:\n",Coefficient_Matrix, "\n")

#Taking input for coloumn Matrix(B)
print("Enter the element of the Coefficient Matrix (B) in a single line (seperated by space):")
Column_Entries = list(map(float,input().split()))
Column_Matrix = np.array(Column_Entries).reshape(NR,1)
print("Column Matrix (B) is as follows:\n",Column_Matrix,"\n")

#Solution of homogenous system of equations using Gauss Jordan
inv_ofcoefficient_matrix = np.linalg.inv(Coefficient_Matrix)
Solution_of_the_system_of_equations = np.matmul(inv_ofcoefficient_matrix,Column_Matrix)
print("Solution of the system of equations using Gauss Jordan")
print(Solution_of_the_system_of_equations)
