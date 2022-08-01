# ! - Con Numpy
# import numpy as np
# print(np.identity(1))
# print(np.identity(2))
# print(np.identity(3))
# testing = np.identity(4)
# print(testing)
# print(testing[0][0])
# print(testing[0][1])
# print(np.identity(5))
# print(np.identity(6))

jaja = [
    [1, 2, 3, 0, 0],
    [4, 5, 6, 0, 0],
    [7, 8, 9, 0, 0],
    [7, 8, 9, 0, 0],
]

print(f"{len(jaja)} X {len(jaja[0])}")

# ! - Con MathFake
from MathFake import MathFake as mf

translation = [
    [1, 0, 0, 500],
    [0, 1, 0, 500],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]

rotation = mf.identity(4)

scale_mat = [
    [100, 0, 0, 0],
    [0, 400, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]

print(f"Translation: {translation}")
print(f"Rotation: {rotation}")
print(f"Scale Mat: {scale_mat}")
print(f"RETURN: {mf.multiply_matrixs([translation, rotation])}")
print(f"RETURN: {mf.multiply_matrixs([translation, rotation, scale_mat])}")
# print(f"RETURN: {translation * rotation * scale_mat}")
        
print("JAJAJA")
number = 4
while number > 0:
    number = number - 1
    print(number)
print("JAJAJA")
# multiply = translation * rotation * scale_mat