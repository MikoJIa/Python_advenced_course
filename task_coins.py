def func_coins(denomination, change):
	to_give_back = [0] * len(denomination)
	count = 0
	for pos, coin in enumerate(reversed(denomination)):
		while coin <= change:
			change -= coin
			to_give_back[pos] += 1
			count += 1
	return count, to_give_back


print(func_coins([1, 2, 5, 8], 17))