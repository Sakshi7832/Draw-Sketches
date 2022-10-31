# install -> pip install sketchpy
from sketchpy import canvas

# draw doremon
obj = canvas.sketch_from_image('C:/Users/dell/Desktop/doremon.jpg')
obj.draw(threshold = 40)
