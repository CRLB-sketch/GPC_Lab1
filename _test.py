from collections import namedtuple
from MathFake import MathFake as mf

V2 = namedtuple('Point2', ['x', 'y'])
V3 = namedtuple('Point3', ['x', 'y', 'z'])
V4 = namedtuple('Point4', ['x', 'y', 'z', 'w'])

tangent_matrix = [
    [ 0.64755284, -0.4061203,  -0.41569427],
    [-0.75890445, -0.26726016, -0.69428498],
    [ 0.06884301,  0.87386401, -0.55794699],
]

tex_normal = [-0.09888687, -0.06724307, 0.99282413]

print(f"JAJAJAJ: {tangent_matrix[1]}")
print(f"RES: {mf.multiply_m3x3_and_m3x1(tangent_matrix, tex_normal)}")
# print(f"RES: {mf.multiply_matrixs([tangent_matrix, tangent_matrix])}")

f = 1 / float((-0.0020000000000000018 * 0.0010000000000000009 - -0.0020000000000000018 * 0.0010000000000000009))
print(f"TESTING: {f}")