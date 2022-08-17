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
    def blue_transparency(render, **kwargs) -> None:
        u, v, w = kwargs["bary_coords"]
        b, g, r = kwargs["v_color"]
        tA, tB, tC = kwargs["tex_coords"]
        nA, nB, nC = kwargs["normals"]
        
        b /= 255
        g /= 255
        r /= 255
        
        if render.active_texture1:
            # P = Au + Bv + Cw
            tU = tA[0] * u + tB[0] * v + tC[0] * w
            tV = tA[1] * u + tB[1] * v + tC[1] * w

            tex_color = render.active_texture1.getColor(tU, tV)

            b *= tex_color[2]
            g *= tex_color[1]
            r *= tex_color[0]
        
        return r, g, b
