def sortedSquaredArray(array):
    # Write your code here.
	negatives = [] # This simulates a stack
	squares = []
	i = 0 
	while i < len(array):
		if array[i] < 0: # If negative
			negatives.append(abs(array[i]))
		else:
			if len(negatives) > 0: # If negatives stack has elements and current element is positive
				top = negatives[-1]
				if i+1 == len(array):
					if top >= array[i]:
						squares.append(array[i] ** 2)
						squares.append(top ** 2)
						negatives.pop()
				else:
					if top >= array[i] and top <= array[i+1]:
						squares.append(array[i] ** 2)
						squares.append(top ** 2)
						negatives.pop()
					else:
						squares.append(array[i] ** 2)
			else:
				squares.append(array[i] ** 2)
		i += 1
	for elem in negatives:
		squares.append(elem ** 2)
	return squares

def sortedSquaredArray2(array):
    # Write your code here.
	squares = []
	leftIndex, rightIndex = 0,len(array)-1 
	while leftIndex <= rightIndex:
		if abs(array[leftIndex]) > abs(array[rightIndex]):
			squares.insert(0,array[leftIndex] ** 2)
			leftIndex += 1
		else:
			squares.insert(0,array[rightIndex] ** 2)
			rightIndex -= 1
	return squares

#array = [-10,-6,-5,1,2,5,6,8]
#array = [1,2,5,5,5,6,8]
#array = [-14,-10,-6,-6,-6,-5]
array = [-14,-10,-6,-6,-6,-5,1,2,5,6,8,12,13]
s = sortedSquaredArray2(array)
print(s)