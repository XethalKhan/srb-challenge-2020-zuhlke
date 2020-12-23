
f = open("./crypto.txt")

encrypted = f.read()

f.close()
#encrypted = "TTTT"

rows = [0] * len(encrypted)

for i in range(1, len(encrypted)):

	for j in range(0, i):

		if encrypted[j] == encrypted[i]:
			rows[i - j] += 1


f = open("key_length.txt", "w")

for i in rows:
	f.write(str(i) + "\n")

f.close()



