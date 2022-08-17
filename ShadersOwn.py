########################################################################################
"""
    Universidad del Valle de Guatemala
    Graficas por Computadora
    Python Render3D
"""
__author__ = "Cristian Laynez 201281"
__status__ = "Student of Computer Science"

# ! Shaders Own : Mis métodos para crear 
########################################################################################

from MathFake import MathFake as mf

"""
Ideas: 
# Wireframe: borde de un triangulo, cordenadas varicentricas # Idea de robot de oro
# Agua: Transparencia y reflexión
# TextureBlend: Multiplicar una textura con otra (Mezcla de texturas)
# Perlin Nouise: Combinar esto mismo con una textura
""" 

class ShadersOwn:

    # Enfocarse en la magnitud de Y (por ejemplo nuevaY = y / render.height)
    @staticmethod
    def color_full_degraded(render) -> None:
        
        return 0, 0, 0

    @staticmethod
    def mixture_textures(render) -> None:

        return 0, 0, 0

    @staticmethod
    def blue_transparency(render) -> None:

        return 0, 0, 0
