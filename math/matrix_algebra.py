from numpy import matrix, linalg, inner, dot

A = matrix([[1,2,3],[2,7,4]])
B = matrix([[1,-1],[0,1]])
C = matrix([[5,-1],[9,1],[6,0]])
D = matrix([[3,-2,-1],[1,2,3]])
u = matrix([6,2,-3,5])
v = matrix([3,5,-1,4])
w = matrix([[1],[8],[0],[5]])

#dimensions (rows, columns)
print(A.shape)
print(B.shape)
print(C.shape)
print(D.shape)
print(u.shape)
print(v.shape)
print(w.shape)

#vector operations
a = 6
print(u + v)
print(u - v)
print(a*u)
print(int(inner(u,v)))
print(linalg.norm(u))

#matrix operations
print('not defined')
print(A - matrix.transpose(C))
print(matrix.transpose(C) + 3*D)
print(dot(B,A))
print('not defined')

#optional
print('not defined')
print(dot(C,B))
print(linalg.matrix_power(B,4))
print(dot(A,matrix.transpose(A)))
print(dot(matrix.transpose(D),D))
