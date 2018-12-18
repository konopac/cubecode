import unreal_engine as ue

# CUBE class
class Cube:

	# constructor
	def __init__(self, name, location):
		self.name = name
		self.location = location
	# end of constructor
	
	# override str()
	def __str__(self):
		return self.name + ': ( x = ' + str(self.location['x']) + ', y = ' + str(self.location['y']) + ' )'
	# end of function
	
	# override repr()
	def __repr__(self):
		return self.name + ': ( x = ' + str(self.location['x']) + ', y = ' + str(self.location['y']) + ' )'
	# end of function

# end of class

# INTERPRETER class
class Interpreter:

	# store current position on the 2D playboard
	currentX = 0
	currentY = 0
	# store the 2D playboard
	playboard = [[0, 0, 0]]
	# store the bounds of the 2D playboard
	lengthX = 0
	lengthY = 0
	
	# interpret the given python code
	def interpret(self, code):
		
		### DEFINE NEEDED FUNCTIONS ##
		
		# roll the cube north
		def roll_north(steps = 1):
			ue.log('roll_north (' + str(steps) + ' steps)')
			for step in range(steps):
				self.currentX += 1
				self.uobject.AddToQueue('roll_north')
		
		# roll the cube south
		def roll_south(steps = 1):
			ue.log('roll_south (' + str(steps) + ' steps)')
			for step in range(steps):
				self.currentX -= 1
				self.uobject.AddToQueue('roll_south')
		
		# roll the cube west
		def roll_west(steps = 1):
			ue.log('roll_west (' + str(steps) + ' steps)')
			for step in range(steps):
				self.currentY -= 1
				self.uobject.AddToQueue('roll_west')
		
		# roll the cube east
		def roll_east(steps = 1):
			ue.log('roll_east (' + str(steps) + ' steps)')
			for step in range(steps):
				self.currentY += 1
				self.uobject.AddToQueue('roll_east')
		
		# check the floor in direction north
		def check_north():
			ue.log('check_north')
			if ((self.currentX + 1) >= self.lengthX) or (not self.playboard[self.currentX + 1][self.currentY]):
				return 0
			return self.playboard[self.currentX + 1][self.currentY].name
		
		# check the floor in direction south
		def check_south():
			ue.log('check_south')
			if ((self.currentX - 1) < 0) or (not self.playboard[self.currentX - 1][self.currentY]):
				return 0
			return self.playboard[self.currentX - 1][self.currentY].name
		
		# check the floor in direction west
		def check_west():
			ue.log('check_west')
			if ((self.currentY - 1) < 0) or (not self.playboard[self.currentX][self.currentY - 1]):
				return 0
			return self.playboard[self.currentX][self.currentY - 1].name
		
		# check the floor in direction east
		def check_east():
			ue.log('check_east')
			if ((self.currentY + 1) >= self.lengthY) or (not self.playboard[self.currentX][self.currentY + 1]):
				return 0
			return self.playboard[self.currentX][self.currentY + 1].name
		
		
		### PREPARE CODE INTERPRETATION ###
		
		ue.log('----------')
		
		# convert actors into python cubes
		cubes = []
		for actor in self.uobject.actors:
			# get name of cube and remove '_C' from the end
			name = actor.get_class().get_name()
			if name.endswith('_C'):
				name = name[:-2]
			# get location of cube
			location = actor.get_actor_location()
			entry = { 'x': int(location.x / 100), 'y': int(location.y / 100) }
			# create cube object and add it to the list
			cubes.append(Cube(name, entry))
		ue.log(cubes)
		
		# measure the bounds of the 2D playboard
		minX = cubes[0].location['x']
		maxX = cubes[0].location['x']
		minY = cubes[0].location['y']
		maxY = cubes[0].location['y']
		for cube in cubes:
			if cube.location['x'] < minX:
				minX = cube.location['x']
			if cube.location['x'] > maxX:
				maxX = cube.location['x']
			if cube.location['y'] < minY:
				minY = cube.location['y']
			if cube.location['y'] > maxY:
				maxY = cube.location['y']
		ue.log('minX = ' + str(minX))
		ue.log('maxX = ' + str(maxX))
		ue.log('minY = ' + str(minY))
		ue.log('maxY = ' + str(maxY))
		
		# create the 2D playboard
		self.lengthX = (maxX - minX) + 1
		self.lengthY = (maxY - minY) + 1
		self.playboard = [[0 for y in range(self.lengthY)] for x in range(self.lengthX)]
		ue.log('lengthX = ' + str(self.lengthX))
		ue.log('lengthY = ' + str(self.lengthY))
		ue.log(self.playboard)
		
		# fill the 2D playboard
		for cube in cubes:
			# shift the cube coordinates to positive values only
			cube.location['x'] = cube.location['x'] - minX
			cube.location['y'] = cube.location['y'] - minY
			ue.log(str(cube.location['x']) + ':' + str(cube.location['y']))
			# set value
			self.playboard[cube.location['x']][cube.location['y']] = cube
			# set start coordinates
			if cube.name == 'StartCube':
				self.currentX = cube.location['x']
				self.currentY = cube.location['y']
		ue.log(self.playboard)
		
		
		###### EXECUTE GIVEN CODE #####
		exec code in globals(), locals()
		###############################
		
		
		# execute queued commands
		self.uobject.PlayQueue()
		ue.log('----------')
	
	# end of function
	
# end of class