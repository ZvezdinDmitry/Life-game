class cell_class(object):
	"""Field's cell of "Life" game"""
	def __init__(self, pos1: int, pos2: int):
		# super(cell, self).__init__()
		self.position = [pos1, pos2]
		self.creature = False
		self.neighbours = 0
		self.creature_temp = False
		self.creature_new = False
	def check_neighbours(self): # Calculating number of neighbours and defining cell with swithing state
		self.creature_temp = self.creature
		self.creature_new = False
		global field
		for i in field:
			for cell in i:
				if (self.position[0] == cell.position[0] + 1 and self.position[1] == cell.position[1]) or (self.position[0] == cell.position[0] + 1 and self.position[1] == cell.position[1] + 1) or (self.position[0] == cell.position[0] + 1 and self.position[1] == cell.position[1] - 1) or (self.position[0] == cell.position[0] and self.position[1] == cell.position[1] + 1) or (self.position[0] == cell.position[0] and self.position[1] == cell.position[1] - 1) or (self.position[0] == cell.position[0] - 1 and self.position[1] == cell.position[1]) or (self.position[0] == cell.position[0] - 1 and self.position[1] == cell.position[1] + 1) or (self.position[0] == cell.position[0] - 1 and self.position[1] == cell.position[1] - 1):
					if cell.creature:
						self.neighbours += 1
		if self.neighbours == 3:
			self.creature_new = True
			self.neighbours = 0
		elif self.neighbours == 2:
			self.neighbours = 0
		else:
			self.creature_temp = False
			self.neighbours = 0
	def final_check(self): # Realization of changings
		if self.creature_temp == False:
			self.creature = False
		if self.creature_new:
			self.creature = True

def extend_right_down(cur_size, field): # Extending field right and down
	cur_size = cur_size
	field = field
	for ind, lst in enumerate(field):
		string = ind + 1
		field[ind].extend([cell_class(string, i) for i in range(cur_size + 1, cur_size + 5)])
	field_new = [[cell_class(j, i) for i in range(1, cur_size + 5)] for j in range(cur_size + 1, cur_size + 5)]
	field.extend(field_new)
	return field

def extend_right_up(cur_size, field): # Extending field right and up
	cur_size = cur_size
	field = field
	for ind, lst in enumerate(field):
		for i, cell in enumerate(field[ind]):
			field[ind][i].position[0] = field[ind][i].position[0] + 4
	for ind, lst in enumerate(field):
		string = ind + 1
		field[ind].extend([cell_class(string + 4, i) for i in range(cur_size + 1, cur_size + 5)])
	field_new = [[cell_class(j, i) for i in range(1, cur_size + 5)] for j in range(1, 5)]
	return field_new + field

def extend_left_down(cur_size, field): # Extending field left and down
	cur_size = cur_size
	field = field
	for ind, lst in enumerate(field):
		for i, cell in enumerate(field[ind]):
			field[ind][i].position[1] = field[ind][i].position[1] + 4
	for ind, lst in enumerate(field):
		string = ind + 1
		new_string = [cell_class(string, i) for i in range(1, 5)]
		field[ind] = new_string + field[ind]
	field_new = [[cell_class(j, i) for i in range(1, cur_size + 5)] for j in range(cur_size + 1, cur_size + 5)]
	return field + field_new

def extend_left_up(cur_size, field): # Extending field left and up
	cur_size = cur_size
	field = field
	for ind, lst in enumerate(field):
		for i, cell in enumerate(field[ind]):
			field[ind][i].position[0] = field[ind][i].position[0] + 4
			field[ind][i].position[1] = field[ind][i].position[1] + 4
	for ind, lst in enumerate(field):
		string = ind + 1
		new_string = [cell_class(string + 4, i) for i in range(1, 5)]
		field[ind] = new_string + field[ind]
	field_new = [[cell_class(j, i) for i in range(1, cur_size + 5)] for j in range(1, 5)]
	return field_new + field

print("Ниже представлены некоторые реализованные сценарии игры 'Жизнь', описанные в журнале 'Квант', а также свободный режим:")
print("1. Блок")
print("2. Навигационные огни")
print("3. Планер")
print("4. Буква 'r'")
print("5. Буква 'H'")
print("6. Крест")
print("7. Космический корабль")
print("8. Пользовательский режим")

scenario = str(input("Выберите сценарий игры, введя его номер в консоль, например '1': ")) # Choosing scenario
while scenario not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
	scenario = str(input("Введенные символы не являются номером сценария, попробуйте еще раз: "))

if scenario == str(1): ### Scenario: Блок
	size = 10
	field = [[cell_class(j, i) for i in range(1, size + 1)] for j in range(1, size + 1)]
	field[3][4].creature = True
	field[3][5].creature = True
	field[4][4].creature = True
	field[4][5].creature = True
	extending = False
elif scenario == str(2): ### Scenario: Навигационные огни
	size = 10
	field = [[cell_class(j, i) for i in range(1, size + 1)] for j in range(1, size + 1)]
	field[4][3].creature = True
	field[3][4].creature = True
	field[4][4].creature = True
	field[4][5].creature = True
	extending = False
elif scenario == str(3): ### Scenario: Планер
	size = 10
	field = [[cell_class(j, i) for i in range(1, size + 1)] for j in range(1, size + 1)]
	field[3][3].creature = True
	field[4][4].creature = True
	field[5][2].creature = True
	field[5][3].creature = True
	field[5][4].creature = True
	extending = True
elif scenario == str(4): ### Scenario: Буква "r"
	size = 10
	field = [[cell_class(j, i) for i in range(1, size + 1)] for j in range(1, size + 1)]
	field[2][4].creature = True
	field[2][5].creature = True
	field[3][3].creature = True
	field[3][4].creature = True
	field[4][4].creature = True
	extending = True
elif scenario == str(5): ### Scenario: Буква "H"
	size = 10
	field = [[cell_class(j, i) for i in range(1, size + 1)] for j in range(1, size + 1)]
	field[3][4].creature = True
	field[3][6].creature = True
	field[4][4].creature = True
	field[4][5].creature = True
	field[4][6].creature = True
	field[5][4].creature = True
	field[5][6].creature = True
	extending = True
elif scenario == str(6): ### Scenario: Крест
	size = 10
	field = [[cell_class(j, i) for i in range(1, size + 1)] for j in range(1, size + 1)]
	field[2][4].creature = True
	field[3][3].creature = True
	field[3][4].creature = True
	field[3][5].creature = True
	field[4][4].creature = True
	field[5][4].creature = True
	extending = True
elif scenario == str(7): ### Scenario: Космический корабль
	size = 10
	field = [[cell_class(j, i) for i in range(1, size + 1)] for j in range(1, size + 1)]
	field[1][4].creature = True
	field[2][5].creature = True
	field[3][1].creature = True
	field[3][5].creature = True
	field[4][2].creature = True
	field[4][3].creature = True
	field[4][4].creature = True
	field[4][5].creature = True
	extending = True
elif scenario == str(8): ### Scenario: Пользовательский
	extending = True
	while True: # Choosing size
		try:
			size = int(input("Укажите стартовый размер игрового поля: "))
			if size <= 0:
				print("Размер поля должен быть больше 0, попробуйте ещё раз")
				continue
			else:
				break
		except ValueError:
			print("Введенные символы не являются целым числом, попробуйте ещё раз")
			continue

	print("Введите через пробел координаты клеток, на которых будут жить существа по паре координат в строке, например: '1 2'. Для окончания ввода, введите 's'")
	field = [[cell_class(j, i) for i in range(1, size + 1)] for j in range(1, size + 1)]
	while True: # Choosing coordinates
		input_ = input()
		if input_ == "s":
			break
		try:
			coordinates = [int(i) for i in input_.split()]
		except ValueError:
			print("Введенные символы не являются целыми числами, попробуйте ещё раз")
			continue
		if len(coordinates) > 2:
			print("Вы ввели слишком много чисел в одной строке, попробуйте ещё раз")
			coordinates = []
			continue
		if coordinates[0] <= 0 or coordinates[1] <= 0:
			print("Можно использовать только положительные числа, попробуйте ещё раз")
			coordinates = []
			continue
		if coordinates[0] > size or coordinates[1] > size:
			print("Введенные координаты находятся за пределами стартового поля, попробуйе ещё раз")
			coordinates = []
			continue
		field[coordinates[0] - 1][coordinates[1] - 1].creature = True
print("Для того, чтобы сделать ход, введите в консоль 'r', для выхода - любой другой символ:")
print(" _"*size + " ")
for i in range(size): # Visualizing field
	line = []
	for cell in field[i]:
		if cell.creature:
			line.append("#")
		else:
			line.append("_")
	line = "|".join(line)
	print(f"|{line}|")
while str(input()) == "r": # Moves
	if extending: # Defining if scenario is extending
		for i in range(size):
			for cell in field[i]:
				if cell.creature and ((size - cell.position[0] < 2 and cell.position[1] >= size / 2) or (size - cell.position[1] < 2 and cell.position[0] >= size / 2)):
					field = extend_right_down(size, field)
					size += 4
				elif cell.creature and ((cell.position[0] < 2 and cell.position[1] >= size / 2) or (size - cell.position[1] < 2 and cell.position[0] < size / 2)):
					field = extend_right_up(size, field)
					size += 4
				elif cell.creature and ((cell.position[0] < 2 and cell.position[1] < size / 2) or (cell.position[1] < 2 and cell.position[0] < size / 2)):
					field = extend_left_up(size, field)
					size += 4
				elif cell.creature and ((size - cell.position[0] < 2 and cell.position[1] < size / 2) or (cell.position[1] < 2 and cell.position[0] >= size / 2)):
					field = extend_left_down(size, field)
					size += 4
	for i in range(size): # Counting amount of neighbours
		for cell in field[i]:
			cell.check_neighbours()
	for i in range(size):
		for cell in field[i]:
			cell.final_check()
	print(" _"*size + " ")
	for i in range(size): # Visualizing field
		line = []
		for cell in field[i]:
			if cell.creature:
				line.append("#")
			else:
				line.append("_")
		line = "|".join(line)
		print(f"|{line}|")