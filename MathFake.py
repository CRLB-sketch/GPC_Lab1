class MathFake:
                    
    @staticmethod
    def identity(size : int):
        # matrix = []
        # for x in range(0, size):
        #     matrix_x = []
        #     for y in range(0, size):                
        #         matrix_x.append(1) if x == y else matrix_x.append(0)                                
        #     matrix.append(matrix_x)
        return [[1 if x == y else 0 for y in range(0, size)] for x in range(0, size)]
    
    @staticmethod
    def multiply_matrixs(all_matrixs : list):       
        print(f"JAJA: {len(all_matrixs)}")
        if len(all_matrixs) <= 1: return None
        for m in all_matrixs:
            if len(m) != len(m[0]): return None            
        size = len(m)
        result = [[ 0 for y in range(0, size)] for x in range(0, size)]        
        for m in range(0, len(all_matrixs)):
            matrix = all_matrixs[m] if m == 0 else result
            next_matrix = all_matrixs[m+1]
            print("+++++++++++++++++++++++++")
            print(f"-> {matrix}")
            print(f"-> {next_matrix}")
            print("-----------")
            for x in range(0, len(matrix)):
                for y in range(0, len(matrix)):
                    res = 0
                    for _ in range(0, len(matrix)):
                        print(f"SEE: {matrix[x][_]} & {next_matrix[_][y]}")
                        res += (matrix[x][_] * next_matrix[_][y])
                    print(f"RES: {res} \n")
                    result[x][y] = res
                print("-------")
            
            print(f"RESULTADO: {result}")
            if (m + 2) == len(all_matrixs): break
            
        return result
    