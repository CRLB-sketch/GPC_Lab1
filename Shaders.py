########################################################################################
"""
    Universidad del Valle de Guatemala
    Graficas por Computadora
    Python Render3D
"""
__author__ = "Cristian Laynez 201281"
__status__ = "Student of Computer Science"

# ! Shaders
# Referencias de Carlos Alonso proporcionado en clase
######################################################################################

from MathFake import MathFake as mf

class Shaders:
    
    @staticmethod
    def gourad(render, **kwargs):
        u, v, w = kwargs["bary_coords"]
        b, g, r = kwargs["v_color"]
        t_a, t_b, t_c = kwargs["tex_coords"]
        n_a, n_b, n_c = kwargs["normals"]

        b /= 255
        g /= 255
        r /= 255
        
        if render.active_texture1:
            t_u = t_a[0] * u + t_b[0] * v + t_c[0] * w
            t_v = t_a[1] * u + t_b[1] * v + t_c[1] * w
            
            tex_color = render.active_texture1.get_color(t_u, t_v)
            
            b *= tex_color[2]
            g *= tex_color[1]
            r *= tex_color[0]
            
        triangle_normal = [
            n_a[0] * u + n_b[0] * v + n_c[0] * w,
            n_a[1] * u + n_b[1] * v + n_c[1] * w,
            n_a[2] * u + n_b[2] * v + n_c[2] * w
        ]
        
        dir_light = [render.dir_light.x, render.dir_light.y, render.dir_light.z]
        
        intensity = mf.dot(triangle_normal, mf.inverse_values_of_array_or_list(dir_light))
        
        b *= intensity
        g *= intensity
        r *= intensity
        
        if intensity > 0:
            return r, g, b
        
        return 0, 0, 0
    
    @staticmethod
    def normal_map(render, **kwargs):
        u, v, w = kwargs["bary_coords"]
        b, g, r = kwargs["v_color"]
        t_a, t_b, t_c = kwargs["tex_coords"]
        n_a, n_b, n_c = kwargs["normals"]
        tangent = kwargs["tangent"]
        bitangent = kwargs["bitangent"]

        b /= 255
        g /= 255
        r /= 255

        # P = Au + Bv + Cw
        t_u = t_a[0] * u + t_b[0] * v + t_c[0] * w
        t_v = t_a[1] * u + t_b[1] * v + t_c[1] * w

        if render.active_texture1:
            tex_color = render.active_texture1.get_color(t_u, t_v)

            b *= tex_color[2]
            g *= tex_color[1]
            r *= tex_color[0]

        triangle_normal = [
            n_a[0] * u + n_b[0] * v + n_c[0] * w,
            n_a[1] * u + n_b[1] * v + n_c[1] * w,
            n_a[2] * u + n_b[2] * v + n_c[2] * w
        ]

        dir_light = [render.dir_light.x, render.dir_light.y, render.dir_light.z]

        if render.normal_map:
            tex_normal = render.normal_map.get_color(t_u, t_v)
            tex_normal = [
                tex_normal[0] * 2 - 1,
                tex_normal[1] * 2 - 1,
                tex_normal[2] * 2 - 1
            ]

            tex_normal = mf.divition(tex_normal, mf.norm(tex_normal))

            tangent_matrix = [
                [tangent[0], bitangent[0], triangle_normal[0]],
                [tangent[1], bitangent[1], triangle_normal[1]],
                [tangent[2], bitangent[2], triangle_normal[2]]
            ]

            # print(f"TANGENT MATRIX: {tangent_matrix}")
            tex_normal = mf.multiply_m3x3_and_m3x1(tangent_matrix, tex_normal) # ! Este es el clavo
            tex_normal = mf.divition(tex_normal, mf.norm(tex_normal))

            intensity = mf.dot(tex_normal, mf.inverse_values_of_array_or_list(dir_light))
        else:
            intensity = mf.dot(triangle_normal, mf.inverse_values_of_array_or_list(dir_light))

        b *= intensity
        g *= intensity
        r *= intensity

        if intensity > 0:
            return r, g, b

        return 0, 0, 0
