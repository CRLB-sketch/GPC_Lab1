from collections import namedtuple
from MathFake import MathFake as mf

V2 = namedtuple('Point2', ['x', 'y'])
V3 = namedtuple('Point3', ['x', 'y', 'z'])
V4 = namedtuple('Point4', ['x', 'y', 'z', 'w'])

# !+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
+++++++++++++++++++++++++++++++++++++++++++
VERTS1: Point3(x=3.7933844, y=-0.403388, z=-8.91156) - VERTS0: Point3(x=3.495088, y=-0.465472, z=-8.557888) + RES EDGE 1: [ 0.2982964  0.062084  -0.353672 ]
VERTS2: Point3(x=3.7246804, y=0.0487572, z=-8.494516) - VERTS0: Point3(x=3.495088, y=-0.465472, z=-8.557888) + RES EDGE 2: [0.2295924 0.5142292 0.063372 ]
+ DELTA0: [0.48, 0.955, 0.0] - DELTA1: [0.489, 0.956, 0.0] - DELTA2: [0.484, 0.97, 0.0]
SUBTRACT (DELTA RES): [0.009 0.001 0.   ] - [0.004 0.015 0.   ]
VALUES: 0.009000000000000008 * 0.015000000000000013 - 0.0040000000000000036 * 0.0010000000000000009
RES F: 7633.587786259529
"""
verts0 = V3(3.495088, -0.465472, -8.557888)
verts1 = V3(3.7933844, -0.403388, -8.91156)
verts2 = V3(3.7246804, 0.0487572, -8.494516)

edge1 = mf.subtract_V3(verts1, verts0)
edge2 = mf.subtract_V3(verts2, verts0)
print(f"EDGE 1: {edge1} & EDGE 2: {edge2}")

tex_coords0 = V3(0.48, 0.955, 0.0)
tex_coords1 = V3(0.489, 0.956, 0.0)
tex_coords2 = V3(0.484, 0.97, 0.0)

delta_uv1 = mf.subtract_V3(tex_coords1, tex_coords0)
delta_uv2 = mf.subtract_V3(tex_coords2, tex_coords0)
print(f"SUBTRACT (DELTA RES): {delta_uv1} | {delta_uv2}")

# !+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# tangent_matrix = [
#     [ 0.64755284, -0.4061203,  -0.41569427],
#     [-0.75890445, -0.26726016, -0.69428498],
#     [ 0.06884301,  0.87386401, -0.55794699],
# ]

# tex_normal = [-0.09888687, -0.06724307, 0.99282413]

# print(f"JAJAJAJ: {tangent_matrix[1]}")
# print(f"RES: {mf.multiply_m3x3_and_m3x1(tangent_matrix, tex_normal)}")
# # print(f"RES: {mf.multiply_matrixs([tangent_matrix, tangent_matrix])}")

# f = 1 / float((-0.0020000000000000018 * 0.0010000000000000009 - -0.0020000000000000018 * 0.0010000000000000009))
# print(f"TESTING: {f}")