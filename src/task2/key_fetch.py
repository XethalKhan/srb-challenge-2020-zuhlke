key_length = 12

#english_freq = [8.2, 1.5, 2.8, 4.3, 13, 2.2, 2, 6.1, 7, 0.15, 0.77, 4, 2.4, 6.7, 7.5, 1.9, 0.095, 6, 6.3, 9.1, 2.8, 0.98, 2.4, 0.15, 2, 0.074]

#Wikipedia page https://en.wikipedia.org/wiki/Letter_frequency

english_freq = [7.8, 2.0, 4.0, 3.8, 11, 1.4, 3, 2.3, 8.6, 0.21, 0.97, 5.3, 2.7, 7.2, 6.1, 2.8, 0.19, 7.3, 8.7, 6.7, 3.3, 1, 0.91, 0.27, 1.6, 0.44]

f = open("./crypto.txt")

encrypted = f.read()

f.close()

for i in range(0, 26):
	english_freq[i] = round(english_freq[i] / 100, 4)

sol = ""

for l in range(0, key_length):
	
	step = 0
	max_freq = 0
	encrypted_freq = [0] * 26
	cnt = 0

	for char in range(l, len(encrypted), key_length):
		encrypted_freq[ord(encrypted[char]) - 65] += 1
		cnt += 1

	encrypted_freq_prob = [0] * 26

	for i in range(0, 26):
		encrypted_freq_prob[i] = round(encrypted_freq[i] / cnt, 4)

	for i in range(0, 26):

		max_temp = 0

		for j in range(0, 26):

			index = 0

			if (i + j) >= 26 :
				index = (i + j) % 26
			else: 
				index = i + j

			max_temp += round(english_freq[j] * encrypted_freq_prob[index], 4)

		if max_temp > max_freq:
			max_freq = max_temp
			step = i

	sol += chr(step + 65)

print(sol)

f = open("./output.txt", "w")
f.write(sol)
f.close()
