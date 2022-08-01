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

rend.gl_load_model("model.obj",
                translate = V3(width/2, height/2, 0),
                scale = V3(300,300,1) )

rend.gl_finish("output.bmp")