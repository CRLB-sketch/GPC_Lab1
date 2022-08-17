########################################################################################
"""
    Universidad del Valle de Guatemala
    Graficas por Computadora
    Python Render3D
"""
__author__ = "Cristian Laynez 201281"
__status__ = "Student of Computer Science"

# ! Shaders : Clase donde se guardará la información del shader a crear
# Referencias de Carlos Alonso proporcionado en clase
######################################################################################

from MathFake import MathFake as mf

class Shaders:
    
    @staticmethod
    def flat(render, **kwargs) -> None:
        u, v, w = kwargs["bary_coords"]
        b, g, r = kwargs["v_color"]
        tA, tB, tC = kwargs["tex_coords"]
        triangle_normal = kwargs["triangle_normal"]

        b /= 255
        g /= 255
        r /= 255

        if render.active_texture1:
            # P = Au + Bv + Cw
            tU = tA[0] * u + tB[0] * v + tC[0] * w
            tV = tA[1] * u + tB[1] * v + tC[1] * w

            text_color = render.active_texture1.getColor(tU, tV)

            b *= text_color[2]
            g *= text_color[1]
            r *= text_color[0]

        dir_light = [render.dir_light.x, render.dir_light.y, render.dir_light.z]
        intensity = mf.dot(triangle_normal, mf.inverse_values_of_array_or_list(dir_light))
        
        b *= intensity
        g *= intensity
        r *= intensity

        if intensity > 0:
            return r, g, b
                
        return 0,0,0
        
    @staticmethod
    def gourad(render, **kwargs):
        
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

            text_color = render.active_texture1.getColor(tU, tV)

            b *= text_color[2]
            g *= text_color[1]
            r *= text_color[0]
            
        triangle_normal = [
            nA[0] * u + nB[0] * v + nC[0] * w,
            nA[1] * u + nB[1] * v + nC[1] * w,
            nA[2] * u + nB[2] * v + nC[2] * w
        ]
        
        dir_light = [render.dir_light.x, render.dir_light.y, render.dir_light.z]
        intensity = mf.dot(triangle_normal, mf.inverse_values_of_array_or_list(dir_light))
        
        b *= intensity
        g *= intensity
        r *= intensity

        if intensity > 0:
            return r, g, b
        
        return 0,0,0

    @staticmethod
    def glow(render, **kwargs):
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

            texColor = render.active_texture1.getColor(tU, tV)

            b *= texColor[2]
            g *= texColor[1]
            r *= texColor[0]

        triangle_normal = [nA[0] * u + nB[0] * v + nC[0] * w,
                            nA[1] * u + nB[1] * v + nC[1] * w,
                            nA[2] * u + nB[2] * v + nC[2] * w]

        dir_light = [render.dir_light.x, render.dir_light.y, render.dir_light.z]
        intensity = mf.dot(triangle_normal, mf.inverse_values_of_array_or_list(dir_light))

        b *= intensity
        g *= intensity
        r *= intensity

        cam_forward = [render.cam_matrix[0][2], render.cam_matrix[1][2], render.cam_matrix[2][2]]

        glow_amount = 1 - mf.dot(triangle_normal, cam_forward)

        if glow_amount <= 0: glow_amount = 0

        # yellow = (1,1,0)

        # b += yellow[2] * glow_amount
        # g += yellow[1] * glow_amount
        # r += yellow[0] * glow_amount
        
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