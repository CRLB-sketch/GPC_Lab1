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
V3 = namedtuple('Point3', ['x', 'y', 'z'])
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

    """
    Valores inversos para un array o lista:
        Los valores de la lista serán opuestos
    Params:
        array or list: Recibir una lista o array con números
    Returns:
        list: La lista con los números opuestos
    """
    @staticmethod
    def inverse_values_of_array_or_list(a_or_l) -> list:        
        return [(-i) for i in a_or_l]

    """
    Dot / Producto Punto:
        Llevar a cabo producto punto de dos listas
    Params:
        a1 & a2: Las listas que se van a operar
    Returns:
        float: Resultado de producto punto
    """
    @staticmethod
    def dot(a1 : list, a2 : list) -> float:
        if len(a1) != len(a2): return None        
        result = 0
        for i in range(0, len(a1)):            
            result += a1[i] * a2[i]                                
        return result
    
    """
    Cross / Producto Cruz:
        Llevar a cabo producto cruz con listas de 3 numeros
    Params:
        a & b: Las listas a operar
    Return:
        list: Lista con el resultado del producto cruz
    """
    @staticmethod
    def cross(a : list, b : list) -> list:
        if len(a) != 3 and len(b) != 3: return None
        i = ((a[1] * b[2]) - (a[2] * b[1]))
        j = ((a[0] * b[2]) - (a[2] * b[0]))
        k = ((a[0] * b[1]) - (a[1] * b[0]))
        return [i, -j, k]
    
    """
    Subtract V3 / Resta de Vectores V3:
        Se restarán dos vectores 3
    Params:
        a & b: Los vectores 3 a operar
    Return:
        list: Resultado de la resta
    """
    @staticmethod
    def subtract_V3(a : V3, b : V3) -> list:        
        return [a.x - b.x, a.y - b.y, a.z - b.z]
    
    """
    Norm / Normalizar:
        Se normalizará una lista dada (puede ser de cualquier tamaño)
    Params:
        data: La lista a normalizar
    Return:
        float: Resultado de la lista normalizada
    """
    @staticmethod
    def norm(data : list) -> float:
        result = 0
        for i in data:
            result += i**2            
        return pow(result, 0.5)
    
    """
    """
    @staticmethod
    def divition(a : list, norm : float):
        return [(i / norm) for i in a]
    