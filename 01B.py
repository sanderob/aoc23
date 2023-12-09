def get_number(s):
	match s:
		case "one":
			return '1'
		case "two":
			return '2'
		case "three":
			return '3'
		case "four":
			return '4'
		case "five":
			return '5'
		case "six":
			return '6'
		case "seven":
			return '7'
		case "eight":
			return '8'
		case "nine":
			return '9'
		case _:
			return ''


with open("./01.txt", 'r') as f:
	sum = 0
	for line in f.readlines():
		first = ""
		last = ""
		fRead = False
		for i in range(0,len(line)):
			for j in range(i+1, len(line)):
				s = line[i:j]
				num = ''
				if 3 <= len(s) <= 5:
					num = get_number(s)
				elif len(s) == 1 and s.isdigit():
					num = s
				if num != '':
					if not fRead:
						first = num
						last = num
						fRead = True
					else:
						last = num
		sum += int(first + last)
print(sum)