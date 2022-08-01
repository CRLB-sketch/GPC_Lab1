########################################################################################
"""
    Universidad del Valle de Guatemala
    Graficas por Computadora
    Python Render3D
"""
__author__ = "Cristian Laynez 201281"
__status__ = "Student of Computer Science"

# ! Math Fake : Clase/Libreria donde estarán las funciones matemáticas y de AL
######################################################################################

from collections import namedtuple
V4 = namedtuple('Point4', ['x', 'y', 'z', 'w'])

class MathFake:
                  
    """ 
    Identity / Identidad:
        Al ingresar un tamaño en específico te crea una matriz identidad

    Params:
        size - int: Tamaño de matriz identidad a crear
    Returns:
        matrix: retorna la nueva matriz identidad
    """  
    @staticmethod
    def identity(size : int) -> list:
        return [[1 if x == y else 0 for y in range(0, size)] for x in range(0, size)]
    
    """ 
    Multiply Matrixs / Multiplicar Matrices:
        Puedes ingresar todas las matrices que se te de la 
        REGALADA gana (siempre y cuando sean del mismo tamaño todos)
        y te lo multiplicará todo :)

    Params:
        all_matrixs - lista: Un listado de todas las matrices a multiplicar
    Returns:
        matrix: retorna el resultado de la multiplicación
    """
    @staticmethod
    def multiply_matrixs(all_matrixs : list) -> list:
        if len(all_matrixs) <= 1: return None
        for m in all_matrixs:
            if len(m) != len(m[0]): return None            
        size = len(m)
        result = [[ 0 for y in range(0, size)] for x in range(0, size)]        
        for m in range(0, len(all_matrixs)):
            matrix = all_matrixs[m] if m == 0 else result
            next_matrix = all_matrixs[m+1]
            for x in range(0, len(matrix)):
                for y in range(0, len(matrix)):
                    res = 0
                    for _ in range(0, len(matrix)):
                        res += (matrix[x][_] * next_matrix[_][y])
                    result[x][y] = float(res)
            if (m + 2) == len(all_matrixs): break            
        return result
    
    """ 
     Multiply Matrix And V4 / Multiplicar Matriz y V4:
        Se verifica si la matriz es 4 x 4

    Params:
        matrix 4x4 - list 4x4: Matriz a operar
        vector4 - V4: Vector4 a operar
    Returns:
        list: retorna el listado con sus correspondiente resultado
    """  
    @staticmethod
    def multiply_matrix_and_v4(matrix_4_x_4 : list, vector4 : V4) -> list:
        if len(matrix_4_x_4) != 4 and len(matrix_4_x_4[0]) != 4:
            return None
                
        v4 = [
            [vector4.x],
            [vector4.y],
            [vector4.z],
            [vector4.w],
        ]
                
        result = [0 for x in range(0, 4)]
        for x in range(0, len(matrix_4_x_4)):
            res = 0
            for y in range(0, len(matrix_4_x_4[x])):
                res += float((matrix_4_x_4[x][y] * v4[y][0]))
            result[x] = res
        
        return result