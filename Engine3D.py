########################################################################################
"""
    Universidad del Valle de Guatemala
    Graficas por Computadora
    Python Render3D
"""
__author__ = "Cristian Laynez 201281"
__status__ = "Student of Computer Science"

# ! Engine 3D : Clase Principal para Iniciar el Render
######################################################################################

from GlRender import *
from Shaders import Shaders as shad
from ShadersOwn import ShadersOwn as shaders
from Texture import Texture

width = 1280
height = 720

rend = Renderer(width, height)

rend.render_background("backgrounds/backgroundP1.bmp")

# ! -----------------------------------------------------
# PROBANDO NORMAL MAP

rend.dir_light = V3(-1, 0, 0)

rend.active_texture1 = Texture("example_models/model.bmp")
rend.normal_map = Texture("example_models/model_normal.bmp")

rend.active_shader = shad.normal_map
rend.gl_load_model(
    "example_models/model.obj",
    translate=V3(-4, 0, -10),
    scale=V3(4, 4, 4),
    rotate=V3(0, 0, 0)
)

rend.active_shader = shad.gourad
rend.gl_load_model(
    "example_models/model.obj",
    translate = V3(4, 0, -10),
    scale = V3(4,4,4),
    rotate = V3(0,0,0)
)

rend.gl_finish("outputs/output.bmp")
