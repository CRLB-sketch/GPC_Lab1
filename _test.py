from collections import namedtuple
from MathFake import MathFake as mf

V2 = namedtuple('Point2', ['x', 'y'])
V3 = namedtuple('Point3', ['x', 'y', 'z'])
V4 = namedtuple('Point4', ['x', 'y', 'z', 'w'])

# !------------------------------------------------
view_port_matrix = [
    [480,    0,    0,    480 ],
    [  0,  270,    0,    270 ],
    [  0,    0,    0.5,  0.5],
    [  0,    0,    0,    1 ]
]
projection_matrix = [
    [ 0.97427858,  0, 0, 0 ],
    [ 0, 1.73205081,  0,          0 ],
    [ 0, 0,         -1.00020002, -0.20002   ],
    [ 0, 0,         -1,          0        ]
]
view_matrix = mf.identity(4)
v = V4(-0.37966500000000003, -3.4910520000000003, -10.023968, 1)

vt = mf.multiply_matrix_and_v4(
            mf.multiply_matrixs(
                [view_port_matrix, projection_matrix, view_matrix]
            ), v)
print(f"PRE 1: {mf.multiply_matrixs([view_port_matrix, projection_matrix])}")
print(f"PRE 2: {mf.multiply_matrixs([view_port_matrix, projection_matrix, view_matrix])}")
print(f"FINAL: {(vt)}")
# # !------------------------------------------------
# # Matriz del ejemplo de la página
# m1 = [
#     [-5, -2, 3, 4],
#     [3, 1, 2, 7],
#     [2, 7, -5, 2],
#     [6, -6, 8, 4],
# ]

# print(f"M1: {mf.linalg_inversion(m1)}")

# # -0.19186046511628 0.16279069767442098 -0.11046511627907163 -0.03779069767442003
# # 0.6453488372093055 -1.0930232558139688 1.0988372093023362 0.7180232558139618
# # 0.7383720930232591 -1.2325581395348981 1.1220930232558244 0.8575581395348918
# # -0.2209302325581408 0.5813953488372148 -0.43023255813953887 -0.3313953488372124

# # Matriz del ejemplo del tutorial de youtube
# m2 = [
#     [2, 1, 3, -2],
#     [3, -4, 2, 5],
#     [1, 6, 2, 1],
#     [-2, 3, -2, 3],
# ]
# print(f"M2: {mf.linalg_inversion(m2)}")

# # -2.533333333333333 0.01666666666666672 1.5499999999999998 -2.233333333333333
# # -0.3999999999999999 -0.049999999999999975 0.3499999999999999 -0.2999999999999999
# # 2.333333333333333 0.08333333333333337 -1.2499999999999998 1.8333333333333333
# # 0.26666666666666666 0.11666666666666667 -0.14999999999999997 0.36666666666666664

# # JAJA!
# m3 = [
#     [1, 0, 0, 0],
#     [0, 1, 0, 0],
#     [0, 0, 1, 0],
#     [0, 0, 0, 1],
# ]
# print(f"M3: {mf.linalg_inversion(m3)}")
# # 1.0 0.0 0.0 0.0
# # 0.0 1.0 0.0 0.0
# # 0.0 0.0 1.0 0.0
# # 0.0 0.0 0.0 1.0

# # !------------------------------------------------
# print("---------------------------------")
# print(f"DIVIDIR ENTRE LISTA Y NORM")
# cross = [-142.491842, 4.91476096, -49.50549084]
# norm = 150.92671577675122
# print(f"RESULT: {mf.divition(cross, norm)}")

# # !------------------------------------------------
# print("---------------------------------")
# print("NORMALIZAR LA LISTA")
# triangle_normal = [139.30538749, -27.51057469, -98.80607576]
# print(f"NORM: {mf.norm(triangle_normal)}") # VALOR ESPERADO: 172.989778053649

# print("---------------------------------")
# print("PRODUCTO CRUZ / CROSS")
# val1 = [ 6.0626,  8.4818, -9.769 ]
# val2 = [16.1834,  6.7782, -3.551 ]

# # RESULTADO ESPERADO
# # [  36.097364  -136.567342   -96.1708468]
# print(f"RESULT 1: {mf.cross(val1, val2)}")

# # !------------------------------------------------
# val1 = [-3.2176, 10.0846, 10.2624]
# val2 = [ 1.6978, 10.0646, -3.8876]

# # RESULTADO ESPERADO
# # [-142.491842      4.91476096  -49.50549084]   
# print(f"RESULT 2: {mf.cross(val1, val2)}")

# # !------------------------------------------------
# val1 = [-13.85536, -10.2706, 7.8982 ]
# val2 = [-3.2176, 10.0846, 10.2624]

# # RESULTADO ESPERADO
# # [-185.05119316  116.77599814 -172.77244602]
# print(f"RESULT 3: {mf.cross(val1, val2)}")

# print("---------------------------------")
# A = V3(514.2194, 329.9992, -83.1232)
# B = V3(520.282, 338.481, -92.8922)
# C = V3(530.4028, 336.7774, -86.6742)
# print(f"SUBSTRACT: {mf.subtract_V3(B, A)}")
# print(f"SUBSTRACT: {mf.subtract_V3(C, A)}")

# print("---------------------------------")
# light = [0, 0, 1]
# print(f"-> NORMAL: {light}")
# print(f"-> INVERSE WITH - : {mf.inverse_values_of_array_or_list(light)}")

# print("---------------------------------")
# print(f"AHORA PRODUCTO PUNTO: ")
# a1 = [1, 2]
# a2 = [3, 4]
# print(f"2 & 2 : {mf.dot(a1, a2)}")

# dir_light = [0, 0, 1]
# triangle_normal = [0.80528103, -0.15903006, -0.57116713]
# print(f"RES DOT 3 & 3: {mf.dot(triangle_normal, mf.inverse_values_of_array_or_list(dir_light))}")

# dir_light = [0, 1]
# triangle_normal = [0.80528103, -0.15903006, -0.57116713]
# print(f"RES DOT INVALID: {mf.dot(triangle_normal, mf.inverse_values_of_array_or_list(dir_light))}")
