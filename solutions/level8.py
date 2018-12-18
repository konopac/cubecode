stepsNorth = 6
stepsEast = 2
for x in range(stepsNorth):
	roll_north()
for x in range(stepsEast):
	roll_east()
for x in range(stepsNorth):
	roll_south()
for x in range(stepsEast):
	roll_east()
for x in range(stepsNorth):
	roll_north()