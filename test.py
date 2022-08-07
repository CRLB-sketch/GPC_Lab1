from collections import namedtuple
from MathFake import MathFake as mf

V2 = namedtuple('Point2', ['x', 'y'])
V3 = namedtuple('Point3', ['x', 'y', 'z'])
V4 = namedtuple('Point4', ['x', 'y', 'z', 'w'])

print("---------------------------------")
print(f"DIVIDIR ENTRE LISTA Y NORM")
cross = [-142.491842, 4.91476096, -49.50549084]
norm = 150.92671577675122
print(f"RESULT: {mf.divition(cross, norm)}")

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
