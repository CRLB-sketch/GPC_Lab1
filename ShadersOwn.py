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
""" 
from random import randrange

pulse = lambda val, dist : ((val*dist)%1) + .5

class ShadersOwn:

    @staticmethod
    def sun_and_moon_light(render, **kwargs) -> None:
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

            tex_color = render.active_texture1.get_color(tU, tV)

            b *= tex_color[2]
            g *= tex_color[1]
            r *= tex_color[0]
        
        triangle_normal = [nA[0] * u + nB[0] * v + nC[0] * w,
                            nA[1] * u + nB[1] * v + nC[1] * w,
                            nA[2] * u + nB[2] * v + nC[2] * w]
        
        d = 0.5
        
        bright = pulse(u, d) + pulse(v, d)
        the_color = [1, 1, 0] if (bright % 2) > 0.5 else [0, 1, 1]
        
        dir_light = [render.dir_light.x, render.dir_light.y, render.dir_light.z]
        diffuse = 0.8 + mf.dot(triangle_normal, dir_light)
        
        b *= the_color[2] * diffuse
        g *= the_color[1] * diffuse
        r *= the_color[0] * diffuse
        
        if b > 1: b = 1
        if g > 1: g = 1
        if r > 1: r = 1
        
        if b < 0: b = 0
        if g < 0: g = 0
        if r < 0: r = 0
        
        return r, g, b

    @staticmethod
    def mixture_textures(render, **kwargs) -> None:
        u, v, w = kwargs["bary_coords"]
        b, g, r = kwargs["v_color"]
        tA, tB, tC = kwargs["tex_coords"]
        nA, nB, nC = kwargs["normals"]
        
        b /= 255
        g /= 255
        r /= 255
        
        triangle_normal = [nA[0] * u + nB[0] * v + nC[0] * w,
                            nA[1] * u + nB[1] * v + nC[1] * w,
                            nA[2] * u + nB[2] * v + nC[2] * w]
                
        
        if render.active_texture1 and render.active_texture2:
            tU = tA[0] * u + tB[0] * v + tC[0] * w
            tV = tA[1] * u + tB[1] * v + tC[1] * w

            tex_color1 = render.active_texture1.get_color(tU, tV)
            tex_color2 = render.active_texture2.get_color(tU, tV)

            b *= (tex_color1[2]) * tex_color2[2]
            g *= (tex_color1[1]) * tex_color2[1]
            r *= (tex_color1[0]) * tex_color2[0]
                        
        return r, g, b

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

            tex_color = render.active_texture1.get_color(tU, tV)

            b *= tex_color[2]
            g *= tex_color[1]
            r *= tex_color[0]
        
        triangle_normal = [nA[0] * u + nB[0] * v + nC[0] * w,
                            nA[1] * u + nB[1] * v + nC[1] * w,
                            nA[2] * u + nB[2] * v + nC[2] * w]

        dir_light = [render.dir_light.x, render.dir_light.y, render.dir_light.z]
        intensity = mf.dot(triangle_normal, mf.inverse_values_of_array_or_list(dir_light))

        b *= intensity
        g *= intensity
        r *= intensity

        cam_forward = [render.cam_matrix[0][2], render.cam_matrix[1][2], render.cam_matrix[2][2]]

        glow_amount = mf.dot(triangle_normal, cam_forward)

        if glow_amount <= 0: glow_amount = 0        
  
        blue = (0, 0, 1)

        b += blue[2] * glow_amount
        g += blue[1] * glow_amount
        r += blue[0] * glow_amount
            
        if b > 1: b = 1
        if g > 1: g = 1
        if r > 1: r = 1

        if intensity > 0:
            return r, g, b
    
        return 0, 0, 0    

    @staticmethod
    def red_diffuse(render, **kwargs) -> None:
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

            tex_color = render.active_texture1.get_color(tU, tV)

            b *= tex_color[2]
            g *= tex_color[1]
            r *= tex_color[0]
           
        triangle_normal = [nA[0] * u + nB[0] * v + nC[0] * w,
                            nA[1] * u + nB[1] * v + nC[1] * w,
                            nA[2] * u + nB[2] * v + nC[2] * w]
        
        dir_light = [render.dir_light.x, render.dir_light.y, render.dir_light.z]
                
        the_color = [0, pulse(v, 10), 1]
        diffuse = 0.5 + mf.dot(triangle_normal, dir_light)
        
        b += the_color[2] * diffuse
        g += the_color[1] * diffuse
        r += the_color[0] * diffuse
        
        if b > 1: b = 1
        if g > 1: g = 1
        if r > 1: r = 1
        
        if b < 0: b = 0
        if g < 0: g = 0
        if r < 0: r = 0
                        
        return r, g, b
    
    @staticmethod
    def tv_cut(render, **kwargs) -> None:
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

            tex_color = render.active_texture1.get_color(tU, tV)

            b *= tex_color[2]
            g *= tex_color[1]
            r *= tex_color[0]
 
        triangle_normal = [nA[0] * u + nB[0] * v + nC[0] * w,
                            nA[1] * u + nB[1] * v + nC[1] * w,
                            nA[2] * u + nB[2] * v + nC[2] * w]
        
        dir_light = [render.dir_light.x, render.dir_light.y, render.dir_light.z]
        
        intensity = mf.dot(triangle_normal, mf.inverse_values_of_array_or_list(dir_light))
    
        black_or_white = randrange(2)
        the_color = [black_or_white, black_or_white, black_or_white]
        
        b += the_color[2] * intensity
        g += the_color[1] * intensity
        r += the_color[0] * intensity
        
        if b > 1: b = 1
        if g > 1: g = 1
        if r > 1: r = 1
        
        if b < 0: b = 0
        if g < 0: g = 0
        if r < 0: r = 0
        
        return r, g, b