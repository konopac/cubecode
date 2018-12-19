for x in range(3):
	roll_north(2)
	if x == 1:
		roll_west(3)
	else:
		roll_east(3)
	roll_north(4)
	if x == 1:
		roll_east(3)
	else:
		roll_west(3)