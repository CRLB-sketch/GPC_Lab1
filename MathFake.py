class MathFake:
                    
    @staticmethod
    def identity(size : int):
        return [[1 if x == y else 0 for y in range(0, size)] for x in range(0, size)]
    
    @staticmethod
    def multiply_matrixs(all_matrixs : list):       
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
    