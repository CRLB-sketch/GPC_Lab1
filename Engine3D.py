########################################################################################
"""
    Universidad del Valle de Guatemala
    Graficas por Computadora
    Python Render3D
"""
__author__ = "Cristian Laynez 201281"
__status__ = "Student of Computer Science"

# ! Engine 3D : Clase Principal para Iniciar el Lab
######################################################################################

from GlRender import *
import random

width = 1920
height = 1080

rend = Renderer(width, height)

# Dibujar el cielo
rend.gl_clear_color(0, 0, 0.1)
rend.gl_clear()

# Dibujar las estrellas
for x in range(width):
    for y in range(height):
        if random.random() > 0.995:
            size = random.randrange(0, 3)

            starColor = color(1, 1, 1)
            
            if size == 1:
                rend.gl_point(x, y, starColor)

            elif size == 1:
                rend.gl_point(x, y, starColor)
                rend.gl_point(x+1, y, starColor)
                rend.gl_point(x+1, y+1, starColor)
                rend.gl_point(x, y+1, starColor)

            elif size == 2:
                rend.gl_point(x, y, starColor)
                rend.gl_point(x, y+1, starColor)
                rend.gl_point(x, y-1, starColor)
                rend.gl_point(x+1, y, starColor)
                rend.gl_point(x-1, y, starColor)

# Dibujar suelo
# circle = [V2(960, 200), V2(1160, 100), V2(950, 10), V2(760, 100)] # Backup Cuadrado Bonito
circle = [
    V2(960, 200), V2(1060, 170), V2(1100, 100),  V2(1160, 0), 
    V2(950, 0), V2(750, 0), V2(815, 100), V2(860, 170) 
] 

rend.draw_polygon(circle, color(0, 0.1, 0))

#Dibujar el arbol 3D
rend.gl_load_model("Tree.obj",
                 translate = V3(width/2, 80, 0),
                 scale = V3(250,250,250))

rend.gl_finish("output.bmp")    