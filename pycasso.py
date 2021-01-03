# pycasso
# goal: generate geometric art
# ideas:
    # pull color pallettes from coolors
    # colors extracted from uploaded image
    # title piece from random word/name generator "verbing the noun"

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import random
import math
from random import randrange
from image_to_palette import *

# configure piece
# palette presets
fish_palette_5      = ['#a97e5d', '#f4eee8', '#abb292', '#10a782', '#079574']
fish_palette_10     = ['#b43c0c', '#a37352', '#b89277', '#f5efeb', '#c9c7ae', '#b0b091', '#6fa579', '#1cb18a', '#05a17d', '#059272']
boygirl_palette_10  = ['#553a25', '#785128', '#8e604a', '#93652d', '#9d6f34', '#998464', '#3d7340', '#539a5b', '#151717', '#a9adb2']
GBH_palette_5       = ['#611915', '#7172ad', '#e697b7', '#d3768e', '#ae5562']
GBH_palette_10      = ['#4a0908', '#7a281c', '#8794d0', '#625e98', '#e99ec0', '#ea86a0', '#c57c9c', '#d76d80', '#b65f6f', '#a2474f']
moonlight_palette_10= ['#0e1a31', '#052c52', '#07345e', '#063b68', '#064374', '#0a4270', '#094c7c', '#1c4e77', '#125988', '#070910']
dogdays_palette_10  = ['#2f2e2e', '#886d2d', '#817d75', '#eaba6d', '#dbd8cb', '#b5b3ad', '#969795', '#ecf0ef', '#111213', '#434c58']
highbeams_palette_8 = ['#fe8e55', '#e19d58', '#fdb57c', '#0239bd', '#0249d3', '#41abf5', '#93d2d8', '#a8dce6']

# set palette to preset
hex_colors = highbeams_palette_8

# set palette to new palette from image (png)
# hex_colors = get_color_pallete('highbeams_EKG.png', 8)

N = 16 # grid side length
figure(num=None, figsize=(10, 10), dpi=120, facecolor='w', edgecolor='k')
plt.axis('off')

# draw triangles
num_triangles = math.ceil(2*N)
for j in range(num_triangles):
    side_length = randrange(math.floor(N/16),N)
    origin_x = randrange(math.floor(-N*3/4), math.ceil(N*3/4))
    origin_y = randrange(math.floor(-N*3/4), math.ceil(N*3/4))
    pt_origin = [origin_x, origin_y]
    vert_delta = random.choice((-1, 1))*side_length
    horz_delta = random.choice((-1, 1))*side_length
    pt_vert = [origin_x, origin_y + vert_delta]
    pt_horz = [origin_x + horz_delta, origin_y]
    pts = [pt_origin, pt_vert, pt_horz]

    i_color = random.randint(0,len(hex_colors)-1)
    color = hex_colors[i_color]

    # color = "#{:06x}".format(random.randint(0, 0xFFFFFF))

    triangle = plt.Polygon(pts, closed=True, color=color)
    plt.gca().add_patch(triangle)

# draw frame
frame_length = N/2
# frame = plt.Rectangle([-frame_length/2, -frame_length/2], frame_length, frame_length, fill = None)
# plt.gca().add_patch(frame)


plt.axis('scaled')
plt.xlim(-frame_length/2, frame_length/2)
plt.ylim(-frame_length/2, frame_length/2)
plt.show()
