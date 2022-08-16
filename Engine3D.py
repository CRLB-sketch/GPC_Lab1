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
from Shaders import Shaders as shaders
from Texture import Texture

# !+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
width = 960
height = 540

rend = Renderer(width, height)

rend.active_texture1 = Texture("models/model.bmp")

model_position = V3(0, 0, -10)

rend.gl_look_at(model_position, V3(-5, -2, 0))

rend.active_shader = shaders.gourad
rend.gl_load_model(
    "models/model.obj", 
    translate= model_position,
    scale=V3(3, 3, 3),
    rotate=V3(0, 0, 0)
)

rend.gl_finish("person_model.bmp")    

# !+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# width = 960
# height = 540

# rend = Renderer(width, height)

# # rend.dir_light = V3(1,0,0)

# rend.active_texture1 = Texture("models/earthDay.bmp")
# rend.active_texture2 = Texture("models/earthNight.bmp")
# rend.active_shader = shaders.flat

# rend.gl_load_model("models/earth.obj",
#                  translate = V3(0, 0, -10),
#                  scale = V3(0.01,0.01,0.01),
#                  rotate = V3(0,90,0))

# !+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# width = 1920
# height = 1080

# rend = Renderer(width, height)

# # rend.active_shader = shaders.gourad
# rend.active_shader = shaders.flat
# rend.active_texture = Texture("models/handgun_S.bmp")

# rend.gl_load_model(
#     "models/GunS.obj",
#     translate = V3(width/2, height/2, 0),
#     rotate = V3(0, 0, 0), 
#     scale = V3(500,500,500)
# )