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
from ShadersOwn import ShadersOwn as shaders
# from Shaders import Shaders as shaders
from Texture import Texture

width = 960
height = 540

rend = Renderer(width, height)

# ! ----------------------------------------------------

rend.active_texture1 = Texture("models/Cat.bmp")

model_position = V3(0, -15, -15)

rend.gl_look_at(model_position, V3(0, -5, 0))

rend.active_shader = shaders.blue_transparency
rend.gl_load_model(
    "models/Cat.obj", 
    translate= model_position,
    scale=V3(0.2, 0.2, 0.2),
    rotate=V3(0, 0, 0)
)

rend.gl_finish("output.bmp")    
