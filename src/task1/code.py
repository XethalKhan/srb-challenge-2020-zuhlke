import math

f = open("./characters.txt", "r")

test = f.read()

f.close()

step = math.floor(len(test) / 2)
length = step

sol = ""

while step >= 1:

	parts = {}

	for i in range(0, len(test) - length + 1):
		key = test[i: i + length]
		if key in parts:
			parts[key]["count"] += 1
			pass
		else:
			parts[key] = {"index": i, "count": 1}

	process = {}

	for k, v in parts.items():
		if v["count"] > 1:
			process[k] = v["index"]

	step = math.floor(step / 2)

	if len(process) == 0:
		parts = {}
		process = {}
		length -= step
	elif len(process) == 1:
		arr = list(process)
		sol = arr[0]
		break
	else:
		parts = {}
		process = {}
		length += step

print(sol)

f = open("./output.txt", "w")
f.write(sol)
f.close()

