if __name__ == "__main__":
	num_tests = int(input())

	for test_idx in range(num_tests):
		line = input().split()
		S = int(line[0]) # Starting bet
		k = int(line[1]) # Number of rounds
		for i in range(k):
			if S % 2 != 0:
				S = S - 15
				S = S % 1000000
				S = S * 2
				S = S % 1000000
			else:
				S = S - 99
				S = S % 1000000
				S = S * 3
				S = S % 1000000
		print(S)