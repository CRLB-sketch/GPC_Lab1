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

# Aplicando Background chido :v
rend.render_background("backgrounds/backgroundP1.bmp")

# Preparando perspectiva de la camara
rend.gl_look_at(V3(0, 0, 0), V3(0, 0, 1))

# ! 1) Australian Dog ------------------------------------------------
rend.active_texture1 = Texture("models/AustralianDog.bmp")
rend.active_shader = shaders.red_diffuse
rend.gl_load_model(
    "models/Dog.obj",
    translate=V3(-0.20, -0.5, 0),
    scale=V3(0.06, 0.06, 0.06),
    rotate=V3(0, 0, 0)
)

# ! 2) Cat  ----------------------------------------------------------
rend.active_texture1 = Texture("models/Cat.bmp")
rend.active_shader = shaders.tv_cut
rend.gl_load_model(
    "models/Cat.obj",
    translate=V3(0.20, -0.4, 0),
    scale=V3(0.005, 0.005, 0.005),
    rotate=V3(0, 0, 0)
)

# ! 3) Iguana --------------------------------------------------------
rend.active_texture1 = Texture("models/Iguana.bmp")
rend.active_shader = shaders.rainbow
rend.gl_load_model(
    "models/Iguana.obj",
    translate=V3(0.75, -0.5, 0),
    scale=V3(0.01, 0.01, 0.01),
    rotate=V3(0, 0, 0)
)

# ! 4) Penguin -------------------------------------    ------------------
rend.active_texture1 = Texture("models/Penguin.bmp")
rend.active_texture2 = Texture("models/handgun_S.bmp")
rend.active_shader = shaders.mixture_textures
rend.gl_load_model(
    "models/PenguinBaseMesh.obj",
    translate=V3(-0.75, -0.5, 0),
    scale=V3(0.2, 0.2, 0.2),
    rotate=V3(0, 0, 0)
)

# ! 5) Eagle ---------------------------------------------------------
rend.active_texture1 = Texture("models/eagle.bmp")
rend.active_shader = shaders.sun_and_moon_light
rend.gl_load_model(
    "models/Eagle.obj",
    translate=V3(0.75, 0.4, 0),
    scale=V3(0.3, 0.3, 0.3),
    rotate=V3(0, 0, 0)
)

rend.gl_finish("outputs/proyecto1_more_shaders.bmp")
