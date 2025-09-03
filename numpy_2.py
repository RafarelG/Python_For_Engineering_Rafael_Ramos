import numpy as np

matrix_3x3 = np.array ([[1,2,3],
                        [4,5,6],
                        [7,8,9]])

matrix_3x3_2 = 2 * matrix_3x3

print(matrix_3x3 * matrix_3x3_2)

A = np.array([[1,2],
              [3,4]])

print(2 * A)
print(A + A)
print(2 * A - 1)  # element-wise scaling and subtraction
print(A / 2 + 5)  # element-wise division and addition

t = np.linspace(0, 10, 20)  # 3 values from 0 to pi
x0 = 5
v = 3
f = x0 + v * t  # position as a function of time
print(f)

a = np.array([-1, -2, -3])
b = np.array([2, 2, 2])
c = np.array([[2],
             [2],
             [2]])
print(a * b)
print(np.multiply(a, b))  # element-wise multiplication
print(np.dot(a, b))  # dot product
print(a @ c)  # dot product

D = np.array([[1, 4, -1],[-1,-3,2],[2,-1,-2]])
E = np.array([-1,2,-2])
x,y,z = np.linalg.solve(D,E)  # solve linear system
print(x,y,z)

norm_D = np.linalg.norm(D)  # vector norm
print(norm_D)
inv_D = np.linalg.inv(D)  # matrix inverse  
print(inv_D)
det_D = np.linalg.det(D)  # matrix determinant

print(inv_D @ E)