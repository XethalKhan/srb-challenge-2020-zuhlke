def optimalCoin(doors):

	ending_coins = 0

	if doors % 2 == 0:
		ending_coins = 4
	else:
		ending_coins = 3

	result = 0

	for i in range(doors - ending_coins, 0, -2):
		result += pow(2, i + 1)

	result += ending_coins

	return result



coins = optimalCoin(10)

f = open("./output.txt", "w")
f.write(str(coins))
f.close()

print(coins)