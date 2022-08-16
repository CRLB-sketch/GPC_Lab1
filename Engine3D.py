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


width = 960
height = 540

rend = Renderer(width, height)

# ! GATO 1 +++++++++++++++++++++++++++++

# rend.active_texture1 = Texture("models/Cat.bmp")

# model_position = V3(0, -15, -15)

# rend.gl_look_at(model_position, V3(-5, -5, 0))

# rend.active_shader = shaders.gourad
# rend.gl_load_model(
#     "models/Cat.obj", 
#     translate= model_position,
#     scale=V3(0.2, 0.2, 0.2),
#     rotate=V3(0, 0, 0)
# )

# rend.gl_finish("cat_medium_shot.bmp")    

# ! GATO 2 +++++++++++++++++++++++++++++
# rend.active_texture1 = Texture("models/Cat.bmp")

# model_position = V3(0, 5, -5)

# rend.gl_look_at(model_position, V3(0, 0, 8))

# rend.active_shader = shaders.gourad
# rend.gl_load_model(
#     "models/Cat.obj", 
#     translate= model_position,
#     scale=V3(0.2, 0.2, 0.2),
#     rotate=V3(0, 0, 0)
# )

# rend.gl_finish("cat_low_angle.bmp")    

# # ! GATO 3 +++++++++++++++++++++++++++++

rend.active_texture1 = Texture("models/Cat.bmp")

model_position = V3(0, -15, -15)

rend.gl_look_at(model_position, V3(0, -5, 0))

rend.active_shader = shaders.gourad
rend.gl_load_model(
    "models/Cat.obj", 
    translate= model_position,
    scale=V3(0.2, 0.2, 0.2),
    rotate=V3(0, 0, 0)
)

rend.gl_finish("cat_high_angle.bmp")    

# # ! GATO 4 +++++++++++++++++++++++++++++

# rend.active_texture1 = Texture("models/Cat.bmp")

# model_position = V3(5, 5, -5)

# rend.gl_look_at(model_position, V3(0, 0, 8))

# rend.active_shader = shaders.gourad
# rend.gl_load_model(
#     "models/Cat.obj", 
#     translate= model_position,
#     scale=V3(0.2, 0.2, 0.2),
#     rotate=V3(0, 0, -20)
# )

# rend.gl_finish("cat_dutch_ancle.bmp")    

# # ! EJEMPLO Y REFERENCIA MODELO +++++++++++++++++++++++++++++
# rend.active_texture1 = Texture("models/model.bmp")

# model_position = V3(0, 0, -10)

# rend.gl_look_at(model_position, V3(-5, -2, 0))

# rend.active_shader = shaders.gourad
# rend.gl_load_model(
#     "models/model.obj", 
#     translate= model_position,
#     scale=V3(3, 3, 3),
#     rotate=V3(0, 0, 0)
# )

# rend.gl_finish("person_model.bmp")    
