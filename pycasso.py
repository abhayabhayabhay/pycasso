# pycasso
# goal: generate geometric art
# ideas:
    # pull color pallettes from coolors
    # colors extracted from uploaded image
    # title piece from random word/name generator "verbing the noun"

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import random
from random import randrange

N = 64 # grid side length
n = 5 # number of sides

figure(num=None, figsize=(10, 10), dpi=120, facecolor='w', edgecolor='k')
plt.axes()

# points = [[2, 1], [8, 1], [8, 4], [6, 8]]
# polygon = plt.Polygon(points, color='#0D324D')
# plt.gca().add_patch(polygon)

for j in range(3):
    pts = []
    n = randrange(3,7)
    for i in range(n+1):
        pts.append([randrange(N), randrange(N)])

    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    polygon = plt.Polygon(pts, color=color)
    plt.gca().add_patch(polygon)


plt.axis('scaled')
plt.show()
