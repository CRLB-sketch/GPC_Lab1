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
from Shaders import Shaders as shaders
from Texture import Texture

width = 1920
height = 1080

rend = Renderer(width, height)

rend.active_shader = shaders.flat
rend.active_texture = Texture("models/model.bmp")

rend.gl_load_model(
    "models/model.obj",
    translate = V3(width/2, height/2, 0),
    rotate = V3(0, 180, 0), 
    scale = V3(200,200,200)
)

rend.gl_finish("output.bmp")    