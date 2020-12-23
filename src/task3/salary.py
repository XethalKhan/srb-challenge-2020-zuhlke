
names_file = open("./names.txt", "r")

names = names_file.read()

names_file.close()

names = names.split(", ")

salary_file = open("./salary.txt", "r")

salary = salary_file.read()

salary_file.close()

salary = salary.split(", ")


total = {}

for i in range(0, len(names)):

	key = names[i]

	if key in total:
		total[key] += int(salary[i])
	else:
		total[key] = int(salary[i])


capt = ""
max_salary = 0

for k, v in total.items():
	if v > max_salary:
		capt = k
		max_salary = v

print(capt)

f = open("./output.txt", "w")
f.write(capt)
f.close()