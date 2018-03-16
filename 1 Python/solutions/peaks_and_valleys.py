###
# peaks_and_valleys.py
# In class solution to lab 18: peaks and valleys
# Takes in as input a list of heights
# Returns the indices of peaks and valleys
###

def peaks(heights):
	"""
	returns the indices of peaks
	"""
	peaks = []
	for i in range(1,len(heights)-1):
		left = heights[i-1]
		middle = heights[i]
		right = heights[i+1]
		if left < middle > right:
			peaks.append(i)
	return peaks


def valleys(heights):
	"""
	returns the indices of valleys
	"""
	valleys = []
	for i in range(1,len(heights)-1):
		left = heights[i-1]
		middle = heights[i]
		right = heights[i+1]
		if left > middle < right:
			valleys.append(i)
	return valleys


def peaks_and_valleys(heights):
	"""
	returns the indices of peaks and valleys in order appearance in the original data
	"""
	p = peaks(heights)
	v = valleys(heights)
	return sorted(p + v)


### Version 2
def draw_mountain(heights):
	peaks = peaks(heights).sort()
	valleys = valleys(heights).sort()
	global_max = peaks[-1]
	global_min = valleys[0]


if __name__ == '__main__':
	data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
	print(data)
	print(peaks(data)) 				# → [6, 14]
	print(valleys(data)) 			# → [9, 17]
	print(peaks_and_valleys(data))	# → [6, 9, 14, 17]
	data = [1, 1, 1, 1, 1]
	print(data)
	print(peaks(data)) 				# → [] empty list
	print(valleys(data)) 			# → []
	print(peaks_and_valleys(data))	# → []
	data = [3, 2, 1, 2, 3]
	print(data)
	print(peaks(data)) 				# → [] empty list
	print(valleys(data)) 			# → [2]
	print(peaks_and_valleys(data))	# → [2]	
	data = [1, 2, 3, 2, 1]
	print(data)
	print(peaks(data)) 				# → [2] 
	print(valleys(data)) 			# → []
	print(peaks_and_valleys(data))	# → [2]	