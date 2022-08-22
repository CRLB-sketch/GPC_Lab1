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
from Texture import Texture

width = 1280
height = 720

rend = Renderer(width, height)

# ! ----------------------------------------------------

rend.active_texture1 = Texture("models/model.bmp")

model_position = V3(0, -15, -15)

rend.gl_look_at(V3(0, 0, 0), V3(0, 0, 1))

# ! MODELO 1 +++++++++++++++++++++++++++++++++++++++++++
rend.active_shader = shaders.red_diffuse
rend.gl_load_model(
    "models/model.obj", 
    translate= V3(0, 0, 0),
    scale=V3(0.2, 0.2, 0.2),
    rotate=V3(0, 0, 0)
)

# ! MODELO 2 +++++++++++++++++++++++++++++++++++++++++++
rend.active_shader = shaders.tv_cut
rend.gl_load_model(
    "models/model.obj", 
    translate= V3(0.35, 0, 0),
    scale=V3(0.2, 0.2, 0.2),
    rotate=V3(0, 0, 0)
)

# ! MODELO 3 +++++++++++++++++++++++++++++++++++++++++++
rend.active_shader = shaders.sun_and_moon_light
rend.gl_load_model(
    "models/model.obj", 
    translate= V3(0.70, 0, 0),
    scale=V3(0.2, 0.2, 0.2),
    rotate=V3(0, 0, 0)
)

# ! MODELO 4 +++++++++++++++++++++++++++++++++++++++++++
rend.active_texture1 = Texture("models/handgun_S.bmp")
rend.active_texture2 = Texture("models/Cat.bmp")
rend.active_shader = shaders.mixture_textures # Trate de hacer el experimento y salio esto xd
rend.gl_load_model(
    "models/model.obj", 
    translate= V3(-0.35, 0, 0),
    scale=V3(0.2, 0.2, 0.2),
    rotate=V3(0, 0, 0)
)

# ! MODELO 5 +++++++++++++++++++++++++++++++++++++++++++
rend.active_texture1 = Texture("models/model.bmp")
rend.active_shader = shaders.blue_transparency
rend.gl_load_model(
    "models/model.obj", 
    translate= V3(-0.70, 0, 0),
    scale=V3(0.2, 0.2, 0.2),
    rotate=V3(0, 0, 0)
)

rend.gl_finish("output.bmp")
# ! ----------------------------------------------------

# rend.active_texture1 = Texture("models/Cat.bmp")

# model_position = V3(0, -15, -15)

# rend.gl_look_at(model_position, V3(-5, -5, 0))

# rend.active_shader = shaders.glow
# rend.gl_load_model(
#     "models/Cat.obj", 
#     translate= model_position,
#     scale=V3(0.2, 0.2, 0.2),
#     rotate=V3(0, 0, 0)
# )

# rend.gl_finish("cat_medium_shot.bmp")    

# ! ----------------------------------------------------
# rend.active_texture1 = Texture("models/Cat.bmp")

# model_position = V3(0, -15, -15)

# rend.gl_look_at(model_position, V3(0, -5, 0))

# rend.active_shader = shaders.blue_transparency
# rend.gl_load_model(
#     "models/Cat.obj", 
#     translate= model_position,
#     scale=V3(0.2, 0.2, 0.2),
#     rotate=V3(0, 0, 0)
# )

# rend.gl_finish("output.bmp")    
