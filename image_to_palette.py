"""
image_to_pallete


adapted from: https://github.com/rodartha/ColorPalette
credits to Colin Page
"""

import os
from PIL import Image, ImageFont, ImageDraw
import matplotlib.pyplot as plt
from scipy import cluster
import pandas as pd
import math
import colorsys
import click

def step(r, g, b, repititions=1):
	lum = math.sqrt(0.241 * r + 0.691 * g + 0.068 * b)

	h, s, v = colorsys.rgb_to_hsv(r, g, b)

	h2 = int(h * repititions)
	lum2 = int(lum * repititions)
	v2 = int(v * repititions)

	if h2 % 2 == 1:
		v2 = repititions - v2
		lum = repititions - lum

	return (h2, lum, v2)
def get_text_height(font, text):
	height = []
	for ch in text:
		height.append(font.getsize(ch)[1])
	return max(height)
def get_text_width(font, text):
	width = 0
	for ch in text:
		width += font.getsize(ch)[0]
	return width
def get_hex_color(color):
    return '#%02x%02x%02x' % color

def get_color_pallete(input_file, num_colors):

    # import image
    img = plt.imread(input_file)

    # create red, green, blue arrays
    red, green, blue = [], [], []

    # within each line
    for line in img:
        # within each pixel in the line
    	for pixel in line:
            # pick out the red, green, blue values and append to array
    		r, g, b, a = pixel
    		red.append(r)
    		green.append(g)
    		blue.append(b)

    # create dataframe and store rgb arrays
    df = pd.DataFrame({
    	'red': red,
    	'green': green,
    	'blue': blue
    })

    # standardize colors?
    df['standardized_red'] = cluster.vq.whiten(df['red'])
    df['standardized_green'] = cluster.vq.whiten(df['green'])
    df['standardized_blue'] = cluster.vq.whiten(df['blue'])

    # use k-mean cluster to define pallete
    color_pallete, distortion = cluster.vq.kmeans(df[['standardized_red', 'standardized_green', 'standardized_blue']], num_colors)
    colors = []

    # find rgb standard deviations
    red_std, green_std, blue_std = df[['red', 'green', 'blue']].std()

    # for each color in the color pallete
    for color in color_pallete:
    	scaled_red, scaled_green, scaled_blue = color
    	colors.append((
    		math.ceil(scaled_red * red_std * 255) ,
    		math.ceil(scaled_green * green_std * 255) ,
    		math.ceil(scaled_blue * blue_std * 255)
    	))

    colors.sort(key=lambda x: step(x[0], x[1], x[2], 8))

    hex_colors = []
    for i in range(len(colors)):
        hex_colors.append(get_hex_color(colors[i]))

    print(hex_colors)
    return hex_colors

def main():
    get_color_pallete('bg.png', 6)

if __name__ == '__main__':
    main()
