from gl import Renderer, color, V2
import random

width = 960
height = 540

rend = Renderer(width, height)

# Sugerencia: Utilizar Bounding

pol1 = [ V2(165, 380), V2(185, 360), V2(180, 330),
         V2(207, 345), V2(233, 330), V2(230, 360),
         V2(250, 380), V2(220, 385), V2(205, 410),V2(193, 383)]

pol2 = [V2(321, 335), V2(288, 286), V2(339, 251), V2(374, 302)]

pol3 = [V2(377, 249), V2(411, 197), V2(436, 249)]

pol4 = [V2(413, 177), V2(448, 159), V2(502, 88), V2(553, 53),
        V2(535, 36),  V2(676, 37),  V2(660, 52), V2(750, 145),
        V2(761, 179), V2(672, 192), V2(659, 214),V2(615, 214),
        V2(632, 230), V2(580, 230), V2(597, 215),V2(552, 214),
        V2(517, 144), V2(466, 180)]

pol5 = [V2(682, 175), V2(708, 120), V2(735, 148), V2(739, 170)]

# Triangulo
rend.drawPolygon(pol3, color(0.5, 0.5, 1))
rend.fillingPolygon(pol3, color(0.5, 0.5, 1))

# # Cuadrado 
# rend.drawPolygon(pol2, color(0.5,1,0.5))

# # Estrella
# rend.drawPolygon(pol1, color(1,0.5,0.5))

# # Poligonos de la jarra
# rend.drawPolygon(pol4, color(1,1,1))
# rend.drawPolygon(pol5, color(1,1,1))

rend.glFinish("output.bmp")