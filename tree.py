import PIL.ImageDraw as ImageDraw,PIL.Image as Image, PIL.ImageShow as ImageShow 
import math
import random

def Deg2rad(angle_deg):
	return (angle_deg * math.pi / 180)


def rotate2D(x1, y1, x2, y2, angle):
	_x2 = x1 - x2
	_y2 = y1 - y2 

	_x2_ = (int)(_x2 * math.cos(angle) + _y2 * math.sin(angle)) + x2
	_y2_ = (int)(_y2 * math.cos(angle) - _x2 * math.sin(angle)) + y2

	return {'x':_x2_, 'y':_y2_}	

def shorten(x1, y1, x2, y2):
	_x = (int)((x1 - x2) / 5 * 4) + x2
	_y = (int)((y1 - y2) / 5 * 4) + y2	
	return {'x':_x, 'y':_y}

def draw_tree(draw, x1, y1, x2, y2, depth):
	if (depth <= 2):
		draw.line((x1, y1, x2, y2), fill=(0,255,0))
	else:
		draw.line((x1, y1, x2, y2), fill=(205,133,63))

	if (depth > 1):
#		angle = Deg2rad(180 - 15)
#		angle2 = Deg2rad(180 + 15)
		angle = Deg2rad(random.randint(150, 180))
		angle2 = Deg2rad(random.randint(180, 230))

		xy = rotate2D(x1, y1, x2, y2, angle)
		xy2 = rotate2D(x1, y1, x2, y2, angle2)

		_xy = shorten(xy['x'], xy['y'], x2, y2)
		_xy2 = shorten(xy2['x'], xy2['y'], x2, y2)

		draw_tree(draw, x2, y2, _xy['x'], _xy['y'], depth - 1)
		draw_tree(draw, x2, y2, _xy2['x'], _xy2['y'], depth - 1)

im = Image.new("RGB", (6000,6000))
draw = ImageDraw.Draw(im)

draw_tree(draw, 3000, 4700, 3000, 4000, 18)
im.show()
