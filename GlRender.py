########################################################################################
"""
    Universidad del Valle de Guatemala
    Graficas por Computadora
    SR2 - Lines
"""
__author__ = "Cristian Laynez 201281"
__status__ = "Student of Computer Science"

"""
    Referencias: 
    Ejemplos de Carlos hecho en clase
"""
# PD: Espero más adelante poder hacerlo en c++ como debe de ser 
######################################################################################

import struct
from collections import namedtuple

V2 = namedtuple('Point2', ['x', 'y'])

def color(r : int, g : int, b : int): return bytes([int(b * 255), int(g * 255), int(r * 255)])

class Renderer(object):
    def __init__(self, width : int, height : int):
        self.__gl_init(width, height)
    
    def __gl_init(self, width : int, height : int):               
        self.__gl_create_window(width, height) 
        self.clearColor = color(0, 0, 0)
        self.currentColor = color(1, 1, 1)   
        self.gl_clear()             

    def __gl_create_window(self, width : int, height : int):
        self.width = width
        self.height = height
        self.gl_view_port(0, 0, self.width, self.height)

    def gl_view_port(self, pos_x : int, pos_y : int, width : int, height : int):
        self.vp_x = pos_x
        self.vp_y = pos_y
        self.vp_width = width
        self.vp_height = height

    def gl_clear_color(self, r : int, g : int, b : int) -> None: self.clearColor = color(r, g, b)

    def gl_color(self, r : int, g : int, b : int) -> None: self.currentColor = color(r,g,b)

    def gl_clear(self) -> None:
        self.pixels = [[ self.clearColor for y in range(self.height)] for x in range(self.width)]

    def gl_clear_viewport(self, clr = None) -> None:
        for x in range(self.vp_x, self.vp_x + self.vp_width):
            for y in range(self.vp_y, self.vp_y + self.vp_height):
                self.gl_point(x, y, clr)

    def gl_point(self, x : int, y : int, clr = None) -> None:
        if ( 0 <= x < self.width) and (0 <= y < self.height):
            self.pixels[x][y] = clr or self.currentColor

    def gl_point_vp(self, ndcX : int, ndcY : int, clr = None) -> None:
        if ndcX < -1 or ndcX > 1 or ndcY < -1 or ndcY > 1:
            return
        x = int((ndcX + 1) * (self.vp_width / 2) + self.vp_x)
        y = int((ndcY + 1) * (self.vp_height / 2) + self.vp_y)        
        self.gl_point(x, y, clr)

    def gl_line(self, v0 : V2, v1 : V2, clr = None) -> None:
        # Implementación del algoritmo de la linea de Bresenham [ y = m * x + b ] 
        x0 = int(v0.x)
        x1 = int(v1.x)
        y0 = int(v0.y)
        y1 = int(v1.y)
        
        # Se dibujará un solo punto si dado caso el punto#0 es igual al punto#1
        if x0 == x1 and y0 == y1:
            self.gl_point(x0, y0, clr)
            return
        
        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        steep = dy > dx

        # Se realizará un intercambio de puntos si la pendiente es mayor a 1 o menor a -1  
        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1
            
        # Se realizará un intercambio de puntos si el punto inicial X es más grande que el punto final X
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        offset = 0
        limit = 0.5
        m = dy / dx
        y = y0

        for x in range(x0, x1 + 1):
            # Dibujar de manera vertical si dado caso la pendendiente es mayor a 1 o meor a -1
            # Si dado caso no se dibujará de manera horizontal
            self.gl_point(y, x, clr) if steep else self.gl_point(x, y, clr)

            offset += m

            if offset >= limit:
                y = y + 1 if y0 < y1 else y - 1                
                limit += 1                
    def draw_polygon(self, polygon : list, clr = None):
        for i in range(len(polygon)):
            self.gl_line(polygon[i], polygon[ (i + 1) % len(polygon)], clr)

    def filling_polygon(self, polygon : list, clr_check, clr_fill):
        x_min = polygon[0].x
        y_min = polygon[0].y
        x_max = polygon[0].x
        y_max = polygon[0].y

        # De primero vamos a obtener los puntos minimos y maximos de los puntos
        for i in range(len(polygon)):
            if polygon[i].x < x_min:
                x_min = polygon[i].x
            if polygon[i].y < y_min:
                y_min = polygon[i].y
            if polygon[i].x > x_max:
                x_max = polygon[i].x
            if polygon[i].y > y_max:
                y_max = polygon[i].y

        central_x = int((x_max + x_min) / 2)
        central_y = int((y_max + y_min) / 2)
        
        def filling_boundary_1(x : int, y : int, clr_check, clr_fill):
            if(self.pixels[x][y] != clr_check):
                self.gl_point(x, y, clr_fill)                
                filling_boundary_1(x , y + 1, clr_fill, clr_check)
                filling_boundary_1(x - 1, y, clr_fill, clr_check)                
                filling_boundary_1(x + 1, y, clr_fill, clr_check)
        
        def filling_boundary_2(x : int, y : int, clr_check, clr_fill):
            if(self.pixels[x][y] != clr_check):
                self.gl_point(x, y, clr_fill)
                filling_boundary_2(x, y - 1, clr_fill, clr_check)
                filling_boundary_2(x - 1, y, clr_fill, clr_check) 
                filling_boundary_2(x + 1, y, clr_fill, clr_check)
                            
        filling_boundary_1(central_x, central_y, clr_check, clr_fill)
        self.gl_point(central_x, central_y, color(0, 0, 0))
        filling_boundary_2(central_x, central_y, clr_check, clr_fill)

    def gl_finish(self, filename : str) -> None:
        word = lambda w : struct.pack('=h', w)
        dword = lambda d : struct.pack('=l', d)
        
        with open(filename, "wb") as file:
            #Header
            pixel = dword( 14 + 40 + (self.width * self.height * 3 )) # Multplicado por 3 porque cada pixel tiene 3 bytes
            header = [bytes('B'.encode('ascii')), bytes('M'.encode('ascii')), pixel, dword(0), dword(14 + 40)]
            for e_header in header: file.write(e_header)
    
            # Info Header
            info_header = [
                dword(40), dword(self.width), dword(self.height), word(1), word(24), dword(0), 
                dword(self.width * self.height * 3), dword(0), dword(0), dword(0), dword(0)
            ]
            for e_info_header in info_header: file.write(e_info_header)
            
            # Pintar toda la tabla
            for y in range(self.height):
                for x in range(self.width):                
                    file.write(self.pixels[x][y])
