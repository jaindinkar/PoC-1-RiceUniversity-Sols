def appendsums(lst):
	for i in range(25):
		sums = lst[i] + lst[i+1] + lst[i+2]
		lst.append(sums)
	return lst

def main():
	sum_three = [0, 1, 2]
	appendsums(sum_three)
	print(sum_three[10])
	print(sum_three[20])

if __name__ == '__main__':
	main()

