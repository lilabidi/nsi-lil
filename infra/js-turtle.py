import js
import inspect
from math import cos, sin, pi, sqrt, atan2
import time

class Turtle:

	""" TODO : les indicateurs de position ne fonctionnent pas car on ne renvoie rien.
	Par exemple, self.state fixe l'appel à self._xcor qui renvoie une donnée.
	"""

	def __init__(self, x = 0, y = 0, angle = 0):
		self.x, self.y = x, y
		self.angle = angle
		self.init_angle = angle
		self.pen_color = 'black'
		self.fill_color = 'black'
		self._pen_down = True
		self.width = 3
		self.canvas = js.document.querySelector('canvas')
		self.ctx = js.document.querySelector('canvas').getContext("2d")
		self.canvas_pt = js.document.getElementById('pointer')
		self.ctx_pt = js.document.getElementById('pointer').getContext("2d")
		self.__set_default()
		self.state = list()     # queue
		self.on_draw = 0
		self.stamp_number = 0
		self.fill = False
		self._speed = 5
		self._hide = False

	def __set_default(self):
		self.ctx.lineJoin = "miter"
		self.ctx.lineCap = "round"
		self.ctx.strokeStyle = self.pen_color
		self.ctx.lineWidth = self.width
		self.style = self.triangle

	def _basic_pointer_draw(function):

		def wrapper(self):
			self.ctx_pt.clearRect(0, 0, self.canvas_pt.width, self.canvas_pt.height)
			self.ctx_pt.beginPath()
			function(self)
			self.ctx_pt.fill()
			self.ctx_pt.stroke()

		return wrapper

	def speed(self, number):
		assert 0 <= number <= 10
		self._speed = number

	def rad2deg(self, angle):
		return angle / pi *180

	def deg2rad(self, angle):
		return angle / 180 * pi

	def hideturtle(self):
		self.state.append({"code" : f"""self._{inspect.currentframe().f_code.co_name}""", "hide" : True})

	def ht(self):
		self.hideturtle()
	
	def _hideturtle(self, params):
		self._hide = params['hide']

	def showturtle(self):
		self.state.append({"code" : f"""self._{inspect.currentframe().f_code.co_name}""", "hide" : False})

	def st(self):
		self.hideturtle()
	
	def _showturtle(self, params):
		self._hide = params['hide']

	def goto(self, x, y):
		self.state.append({"code" : f"""self._{inspect.currentframe().f_code.co_name}""", "x" : x, "y" : y})

	def _goto(self, params):
		x, y = params["x"], params["y"]
		if self._pen_down : 
			self.ctx.beginPath()
			self.ctx.moveTo(self.x, self.y)
			self.ctx.lineTo(x, y)
			self.ctx.stroke()
		self.x, self.y = x, y
		if (not self._hide): self.style()

	def _get_parameters(self, x, y):
		if y is not None : 
			x2, y2 = x, y
		elif isinstance(x, Turtle): 
			x2, y2 = Turtle.x, Turtle.y 
		else :
			x2, y2 = x
		return x2, y2

	def towards(self, x, y = None):
		""" Fonction à revoir ?"""
		self.state.append({"code" : f"""self._{inspect.currentframe().f_code.co_name}""", "x" : x, "y" : y})

	def _towards(self, params):
		x2, y2 = self._get_parameters(params["x"], params["y"])
		return (self.rad2deg(atan2(self.y-y2, self.x-x2)) + 180) % 360

	def distance(self, x, y = None):
		self.state.append({"code" : f"""self._{inspect.currentframe().f_code.co_name}""", "x" : x, "y" : y})

	def _distance(self, x, y = None):
		x2, y2 = self._get_parameters(params["x"], params["y"])
		return sqrt((self.x-x2)**2 + (self.y-y2)**2)

	def pencolor(self, r = None, g = None, b = None):
		self.state.append({"code" : f"""self._{inspect.currentframe().f_code.co_name}""", "r" : r, "g" : g, "b" : b})

	def _pencolor(self, params):
		r, g, b = params["r"], params["g"], params["b"]
		if isinstance(r, str) :
			color = r
		elif isinstance(r, tuple) :
			rr, g, b = r
			color = self.rgb2hex(rr, g, b)
		elif g is not None and b is not None :
			color = self.rgb2hex(r, g, b)
		elif r is None:
			return self.pen_color
		self.pen_color = color
		self.ctx.strokeStyle = color
		self.ctx_pt.strokeStyle = color

	def fillcolor(self, r = None, g = None, b = None):
		self.state.append({"code" : f"""self._{inspect.currentframe().f_code.co_name}""", "r" : r, "g" : g, "b" : b})

	def _fillcolor(self, params):
		r, g, b = params["r"], params["g"], params["b"]
		if isinstance(r, str) :
			color = r
		elif isinstance(r, tuple) :
			rr, g, b = r
			color = self.rgb2hex(rr, g, b)
		elif g is not None and b is not None :
			color = self.rgb2hex(r, g, b)
		elif r is None:
			return self.fill_color
		self.fill_color = color
		self.ctx.fillStyle = color
		self.ctx_pt.fillStyle = color

	def color(self, r1 = None, g1 = None, b1 = None, r2 = None, g2 = None, b2 = None):
		self.state.append({"code" : f"""self._{inspect.currentframe().f_code.co_name}""", \
							"r1" : r1, "g1" : g1, "b1" : b1, "r2" : r2, "g2" : g2, "b2" : b2 })

	def _color(self, params):
		r1, g1, b1 = params["r1"], params["g1"], params["b1"]
		r2, g2, b2 = params["r2"], params["g2"], params["b2"]
		if r1 is None and r2 is None:
			return self.pen_color, self.fill_color
		elif isinstance(r1, str) and isinstance(g1, str): 
			new_pen_params = {"r" : r1, "g":None, "b": None}
			new_fill_params = {"r" : g1, "g":None, "b": None}
			self._pencolor(new_pen_params)
			self._fillcolor(new_fill_params)
		elif isinstance(r1, tuple) and isinstance(g1, tuple): 
			new_pen_params = {"r" : r1, "g":None, "b": None}
			new_fill_params = {"r" : g1, "g":None, "b": None}
			self._pencolor(new_pen_params)
			self._fillcolor(new_fill_params)
		elif isinstance(r1, str) and g1 is None:
			new_params = {"r" : r1, "g":None, "b": None}
			self._pencolor(new_params)
			self._fillcolor(new_params)
		elif isinstance(r1, tuple) and g1 is None:
			new_params = {"r" : r1, "g":None, "b": None}
			self._pencolor(new_params)
			self._fillcolor(new_params)
		elif r1 is not None and g1 is not None and b1 is not None and r2 is None: 
			new_params = {"r" : r1, "g":g1, "b": b1}
			self._pencolor(new_params)
			self._fillcolor(new_params)

	#def _determine_colors(self, r, g, b):

	def rgb2hex(self, r, g, b):
		for i in [r, g, b]:
			assert 0 <= i <= 255, "Wrong color code"
		return '#%02x%02x%02x' % (r, g, b)

	def pensize(self, width = None):
		self.state.append({"code" : f"""self._{inspect.currentframe().f_code.co_name}""", "width" : width })

	def width(self, width = None):
		self.pensize(width)

	def _pensize(self, params):
		width = params["width"]
		if (width is None): return self.ctx.lineWidth
		self.ctx.lineWidth = width

	def pendown(self):
		self.state.append({"code" : f"""self._{inspect.currentframe().f_code.co_name}"""})

	def pd(self):
		self.pendown()

	def down(self):
		self.pendown()

	def _pendown(self, params):
		self._pen_down = True

	def penup(self):
		self.state.append({"code" : f"""self._{inspect.currentframe().f_code.co_name}"""})

	def up(self):
		self.penup()

	def pu(self):
		self.penup()

	def _penup(self, params):
		self._pen_down = False

	def shape(self, style = None):
		self.state.append({"code" : f"""self._{inspect.currentframe().f_code.co_name}""", "sh" : style})
	
	def _shape(self, params):
		style = params["sh"]
		dico_style = {'arrow' : self.arrow, 'turtle' : self.turtle, \
			'circle' : self.cercle, 'square' : self.square, \
			'triangle' : self.triangle, 'classic': self.arrow}
		self.style = dico_style[style]

	def forward(self, L):
		if self._speed == 0 : 
			self.state.append({"code" : f"""self._{inspect.currentframe().f_code.co_name}""", "L" : L })
		else :
			for _ in range(0, L, self._speed):
				self.state.append({"code" : f"""self._{inspect.currentframe().f_code.co_name}""", "L" : self._speed})
			self.state.append({"code" : f"""self._{inspect.currentframe().f_code.co_name}""", "L" : L % self._speed})

	def fd(self, L):
		self.forward(L)
				
	def _forward(self, params):
		L = params["L"]
		if self.fill : self.fill_coordinates.append((self.x, self.y))
		self.ctx.beginPath()
		if (not self._hide): self.style()
		self.ctx.moveTo(self.x, self.y)
		self.ctx.lineTo(self.x + L * cos(self.deg2rad(self.angle)), \
						self.y + L * sin(self.deg2rad(self.angle)))
		if self._pen_down: self.ctx.stroke()
		self.x += L * cos(self.deg2rad(self.angle))
		self.y += L * sin(self.deg2rad(self.angle))

	def backward(self, L):
		if self._speed == 0 : 
			self.state.append({"code" : f"""self._{inspect.currentframe().f_code.co_name}""", "L" : -L })
		else :
			for _ in range(0, L, self._speed):
				self.state.append({"code" : f"""self._{inspect.currentframe().f_code.co_name}""", "L" : -self._speed})
			self.state.append({"code" : f"""self._{inspect.currentframe().f_code.co_name}""", "L" : -L % self._speed})

	def back(self, L):
		self.backward(L)

	def bk(self, L):
		self.backward(L)

	def _backward(self, params):
		L = params["L"]
		if self.fill : self.fill_coordinates.append((self.x, self.y))
		self.ctx.beginPath()
		if (not self._hide): self.style()
		self.ctx.moveTo(self.x, self.y)
		self.ctx.lineTo(self.x + L * cos(self.deg2rad(self.angle)), \
						self.y + L * sin(self.deg2rad(self.angle)))
		if self._pen_down: self.ctx.stroke()
		self.x += L * cos(self.deg2rad(self.angle))
		self.y += L * sin(self.deg2rad(self.angle))

	def xcor(self):
		""" non fonctionnel """
		self.state.append({"code" : f"""self._{inspect.currentframe().f_code.co_name}"""})

	def _xcor(self, params):
		return self.x

	def ycor(self):
		""" non fonctionnel """
		self.state.append({"code" : f"""self._{inspect.currentframe().f_code.co_name}"""})

	def _ycor(self):
		return self.y

	def heading(self):
		self.state.append({"code" : f"""self._{inspect.currentframe().f_code.co_name}"""})

	def _heading(self):
		return self.angle

	def setheading(self, angle):
		self.state.append({"code" : f"""self._{inspect.currentframe().f_code.co_name}""", "a" : angle})

	def seth(self, angle):
		self.setheading(angle)

	def _setheading(self, params):
		angle = params["a"]
		self.angle = angle

	def setx(self, x):
		self.state.append({"code" : f"""self._{inspect.currentframe().f_code.co_name}""", "x" : x})

	def _setx(self, params):
		x = params["x"]
		self.x = x

	def sety(self, y):
		self.state.append({"code" : f"""self._{inspect.currentframe().f_code.co_name}""", "y" : y})

	def _setx(self, params):
		y = params["y"]
		self.y = y

	def home(self):
		self.state.append({"code" : f"""self._{inspect.currentframe().f_code.co_name}"""})

	def _home(self, params):
		self.x, self.y, self.angle = 0, 0, self.init_angle

	def begin_fill(self):
		self.state.append({"code" : f"""self._{inspect.currentframe().f_code.co_name}"""})

	def _begin_fill(self, *args):
		self.fill_coordinates = []
		self.fill = True

	def end_fill(self):
		self.state.append({"code" : f"""self._{inspect.currentframe().f_code.co_name}"""})

	def _end_fill(self, *args):
		self.ctx.fillStyle = self.fill_color
		for ptX, ptY in self.fill_coordinates:
			self.ctx.lineTo(ptX, ptY)
		self.ctx.fill("evenodd")
		self.fill = False

	def filling(self):
		return self.fill

	@_basic_pointer_draw
	def triangle(self):
		x, y = self.x, self.y
		x1, y1 = self.rotation(-15, -10)
		x2, y2 = self.rotation(-15, 10)
		self.ctx_pt.moveTo(x, y)
		self.ctx_pt.lineTo(x+x1, y+y1)
		self.ctx_pt.lineTo(x+x2, y+y2)

	@_basic_pointer_draw
	def arrow(self):
		x, y = self.x, self.y
		x1, y1 = self.rotation(-15, -8)
		x2, y2 = self.rotation(-15, 8)
		x3, y3 = self.rotation(-10, 0)
		self.ctx_pt.moveTo(x, y)
		self.ctx_pt.lineTo(x+x1, y+y1)
		self.ctx_pt.lineTo(x+x3, y+y3)
		self.ctx_pt.lineTo(x+x2, y+y2)

	@_basic_pointer_draw
	def turtle(self):
		x, y = self.x, self.y
		quarter_turtle = [(-5,2), (-6,4), (-5,5), (-4,3)] 
		half_head = [(5,1), (7,2)] 
		half_turtle = quarter_turtle + [(-1,4)] \
			+ [self._x_symmetry(p, q, -1) for (p,q) in quarter_turtle[::-1]] \
			+ half_head
		full_turtle = [(-6,0)] + half_turtle + [(9,0)] \
			+ [self._y_symmetry(p, q, 0) for (p,q) in half_turtle[::-1]]
		rotated_full_turtle = [self.rotation(p, q) for (p, q) in full_turtle]
		rotated_full_turtle = [self._stretch(p, q) for (p, q) in rotated_full_turtle]
		
		self.ctx_pt.moveTo(x + rotated_full_turtle[0][0], y + rotated_full_turtle[0][1])
		for (p,q) in rotated_full_turtle:
			self.ctx_pt.lineTo(x + p, y + q)
	
	def _stretch(self, x, y, stretch_factor=2):
		return (x*stretch_factor, y*stretch_factor)

	@_basic_pointer_draw            
	def cercle(self):
		rad = 15
		x, y = self.x, self.y
		self.ctx_pt.arc(x, y, rad, 0, 2*pi)

	@_basic_pointer_draw
	def square(self):
		side = 15
		x, y = self.x, self.y
		x0, y0 = self.rotation(-side/2, -side/2)
		x1, y1 = self.rotation(-side/2, side/2)
		x2, y2 = self.rotation(side/2, -side/2)
		x3, y3 = self.rotation(side/2, side/2)
		self.ctx_pt.moveTo(x+x0, y+y0)
		self.ctx_pt.lineTo(x+x1, y+y1)
		self.ctx_pt.lineTo(x+x3, y+y3)
		self.ctx_pt.lineTo(x+x2, y+y2)

	def _x_symmetry(self, x, y, x_axis):
		return (2*x_axis-x, y)

	def _y_symmetry(self, x, y, y_axis):
		return (x, 2*y_axis-y)

	def rotation(self, x, y):
		inv_rot_mat = [[cos(self.deg2rad(self.angle)), -sin(self.deg2rad(self.angle))], \
					[sin(self.deg2rad(self.angle)), cos(self.deg2rad(self.angle))]]
		new_x = inv_rot_mat[0][0]*x + inv_rot_mat[0][1]*y
		new_y = inv_rot_mat[1][0]*x + inv_rot_mat[1][1]*y
		return new_x, new_y

	def circle(self, radius, extent = None, steps = None):
		#coords = self._get_circle_coordinates(radius)
		#n = 12
		#for i in range(n):
		#    self.state.append({"code": f"""self._{inspect.currentframe().f_code.co_name}""", \
		#                       "x" : coords[i][0], "y" : coords[i][1]})
		self.state.append({"code": f"""self._{inspect.currentframe().f_code.co_name}""", \
								"r": radius, "e":extent , "s":steps})
		
	def _circle(self, params):
		#self._goto(params)
		
		radius, extent, steps = params["r"], params["e"], params["s"]
		n = 12
		eps = 1
		if radius < 0 : radius, eps = -radius, -1
		center = [self.x+radius*cos(self.deg2rad(self.angle - 90)), \
						self.y+radius*sin(self.deg2rad(self.angle - 90))]
		if extent is None and steps is None:
			angle = [eps*i*360/n-90 for i in range(n)]
			coords = [(radius*cos(self.deg2rad(angle[i])), radius*sin(self.deg2rad(angle[i]))) for i in range(n)]
			self.ctx.clearRect(0, 0, self.canvas_pt.width, self.canvas_pt.height)
			self.ctx.beginPath()
			self.ctx.moveTo(center[0]+coords[0][0], center[1]+coords[0][1])
			for i in range(1, n):
				self.ctx.lineTo(center[0]+coords[i][0], center[1]+coords[i][1])
			self.ctx.closePath()
			self.ctx.stroke()
		#elif steps is None:

		#else:

	#def _get_circle_coordinates(self, radius):
	#   n = 12
	#   eps = 1
	#   if radius < 0 : radius, eps = -radius, -1
	#   center = [self.x+radius*cos(self.deg2rad(self.angle - 90)), \
		#           self.y+radius*sin(self.deg2rad(self.angle - 90))]
		#angle = [eps*i*360/n-90 for i in range(n)]
		#coords = [(center[0] +radius*cos(self.deg2rad(angle[i])), center[1] +radius*sin(self.deg2rad(angle[i]))) for i in range(n)]
		#return coords

	def right(self, angle):
		if self._speed == 0 : 
			self.state.append({"code": f"""self._{inspect.currentframe().f_code.co_name}""", "a": angle})
		else :
			for _ in range(angle//self._speed):
				self.state.append({"code": f"""self._{inspect.currentframe().f_code.co_name}""", "a": self._speed})
			self.state.append({"code": f"""self._{inspect.currentframe().f_code.co_name}""", "a": angle % (self._speed)})

	def rt(self, angle):
		self.right(angle)

	def left(self, angle):
		if self._speed == 0 : 
			self.state.append({"code": f"""self._{inspect.currentframe().f_code.co_name}""", "a": angle})
		else :
			for _ in range(angle//self._speed):
				self.state.append({"code": f"""self._{inspect.currentframe().f_code.co_name}""", "a": self._speed})
			self.state.append({"code": f"""self._{inspect.currentframe().f_code.co_name}""", "a": angle % (self._speed)})

	def lt(self, angle):
		self.left(angle)

	def _right(self, params):
		angle = params["a"]
		self.angle += angle
		if (not self._hide): self.style()

	def _left(self, params):
		angle = params["a"]
		self.angle -= angle
		if (not self._hide): self.style()

	#def stamp(self):
	#    self.stamp_number += 1
	#    self.ctx.triangle()
	#    return self.stamp_number

	def dot(self, size = None, color = None):
		if isinstance(size, str) : size, color = None, size
		self.state.append({"code": f"""self._{inspect.currentframe().f_code.co_name}""", "size": size, "color": color})

	def _dot(self, params):
		# dot is not always on top of the line
		color = params["color"]
		size = params["size"]/2 if params["size"] is not None else max(self.ctx.lineWidth+4, self.ctx.lineWidth*2)
		assert size >= 1, f"""bad screen distance {size}"""
		self.ctx.beginPath()
		self.ctx.arc(self.x, self.y, size, 0, 2*pi)
		self.ctx.fillStyle = color if color is not None else self.color
		self.ctx.fill()

	def position(self):
		self.state.append({"code" : f"""self._{inspect.currentframe().f_code.co_name}"""})
	
	def _position(self, *args):
		return (self.x, self.y)

	def pos(self):
		self.position()     

	def tick(self):
		# Clear canvas
		if len(self.state) > 0 :	
			# Draw current state
			commands = self.state.pop(0)
			command = commands.pop("code")
			params = commands
			eval(command)(params)
		else : 
			js.clearInterval(self.on_draw)

	def mainloop(self):
		self.ctx.clearRect(0, 0, self.canvas.width, self.canvas.height)
		self.ctx_pt.clearRect(0, 0, self.canvas_pt.width, self.canvas_pt.height)
		self._animate()

	def _mainloop_noclear(self):
		self._animate()            

	def _animate(self):
		self.on_draw = js.window.setInterval(lambda x=2 : self.tick(), 10)

_direct_access_turtle = Turtle()
def _deco_direct_access(function):

	def wrapper(*args):
		global _direct_access_turtle
		function(*args)
		_direct_access_turtle._mainloop_noclear()

	return wrapper


method_list = [func for func in dir(Turtle) if callable(getattr(Turtle, func)) and not func.startswith("_")]

for nom in method_list:
	exec(f"""@_deco_direct_access\ndef {nom}(*args):\n\t_direct_access_turtle.{nom}(*args)""")
