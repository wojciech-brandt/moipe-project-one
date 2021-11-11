import numpy as np

def border_values(arr: np.ndarray) -> tuple:
	return (arr[0], arr[-1])

def max_value(arr: np.ndarray):
	max = arr[0]
	for i in arr:
		if i > max: max = i
	
	return max

def min_value(arr: np.ndarray):
	min = arr[0]
	for i in arr: 
		if i < min: min = i

	return min

def arr_sum(arr: np.ndarray):
	sum = 0
	for i in arr: sum = sum + i
	
	return sum

def arr_average(arr: np.ndarray): return arr_sum(arr)/arr.size

def variance(arr: np.ndarray): 
	av = arr_average(arr)
	sum = 0
	for i in arr:
		sum = sum + (i - av)**2
	
	return ( (1/ (arr.size - 1) ) * sum )

def standard_deviation(arr: np.ndarray): 
	return np.sqrt(variance(arr))
