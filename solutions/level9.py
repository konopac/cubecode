steps = 6
for x in range(3):
	for y in range(steps):
		roll_north()
	roll_east()
	roll_east()
	for y in range(steps):
		roll_south()
	roll_east()
	roll_east()
	steps = steps - 2