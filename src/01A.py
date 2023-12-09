

with open("../resources/01.txt", 'r') as f:
	sum = 0
	for line in f.readlines():
		first = ""
		last = ""
		fRead = False
		for char in line:
			if char.isdigit():
				if not fRead:
					first = char
					last = char
					fRead = True
				else:
					last = char
		num = int(first + last)
		sum += num
print(sum)