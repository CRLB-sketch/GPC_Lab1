from collections import namedtuple
V4 = namedtuple('Point4', ['x', 'y', 'z', 'w'])
class Matrix(list):
    # Matrix multiplication A @ B
    def __matmul__(self, B):
        print("ACTIVATE")
        self = A
        
        N = len(A)
        M = len(A[0])
        P = len(B[0])
        
        result = []
        for i in range(N):
            row = [0] * P
            result.append(row)
            
        for i in range(N):
            for j in range(P):
                for k in range(M):
                    result[i][j] += A[i][k] * B[k][j]
        return result
        
# Example
A = Matrix([[2, 0],[1, 9]])
B = Matrix([[3, 9],[4, 7]])
print("JAJA")
print(A @ B)
print("---------------------")

matrix_jeje = [
    [100, 0, 0, 500],
    [0, 400, 0, 500],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]
v = V4(0.193131, -0.106435, 0.533575, 1)

vt = A @ v
print(f"VT: {vt}")

# # ! - Con MathFake
# from MathFake import MathFake as mf

# translation = [
#     [1, 0, 0, 500],
#     [0, 1, 0, 500],
#     [0, 0, 1, 0],
#     [0, 0, 0, 1]
# ]

# rotation = mf.identity(4)

# scale_mat = [
#     [100, 0, 0, 0],
#     [0, 400, 0, 0],
#     [0, 0, 1, 0],
#     [0, 0, 0, 1]
# ]

# print(f"Translation: {translation}")
# print(f"Rotation: {rotation}")
# print(f"Scale Mat: {scale_mat}")
# print(f"RETURN: {mf.multiply_matrixs([translation, rotation])}")
# print(f"RETURN: {mf.multiply_matrixs([translation, rotation, scale_mat])}")
        
# print("JAJAJA")
# number = 4
# while number > 0:
#     number = number - 1
#     print(number)
# print("JAJAJA")
