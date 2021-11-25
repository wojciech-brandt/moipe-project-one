import numpy as np
import custom_statistics as stat

def polynomial_approximation(
	Xarr: np.ndarray, 
	Yarr: np.ndarray,
	deg: np.int8
) -> np.array:
	"""
	Calculate a vector of values that approximate the corresponding 'Yarr' values
	using a polynomial function.
	
	Parameters
	----------
	Xarr : np.ndarray
		Vector of x values
	Yarr : np.ndarray
		Vector of y values that corresponds to Xarr; must be the same size as Xarr
	deg : np.int8
		The approximating polynomial's degree, +1
		
	Returns
	-------
	np.ndarray
		A vector of values calculated based on the approximating function."""
	
	X_vec = np.zeros([Yarr.size, deg])

	for i in np.arange(deg):
		X_vec[:, i] = Xarr**i

	A_vec = np.linalg.inv( np.transpose(X_vec) @ X_vec ) @ np.transpose(X_vec) @ Yarr
	return np.array([X_vec @ A_vec, A_vec], dtype=object)  

def natlog_approximation(
	Xarr: np.ndarray,
	Yarr: np.ndarray,
	deg: np.int8
) -> np.array:
	"""
	Calculate a vector of values that approximate the corresponding 'Yarr' values
	using a natural logarythm function.
	
	Parameters
	----------
	Xarr : np.ndarray
		Vector of x values
	Yarr : np.ndarray
		Vector of y values that corresponds to Xarr; must be the same size as Xarr
	deg : np.int8
		The approximating function's degree, +1
		
	Returns
	-------
	np.ndarray
		A vector of values calculated based on the approximating function."""

	X_vec = np.zeros([Yarr.size, deg])

	for i in np.arange(deg):
		X_vec[:, i] = np.log(Xarr)**i

	A_vec = np.linalg.inv( np.transpose(X_vec) @ X_vec ) @ np.transpose(X_vec) @ Yarr
	return np.array([X_vec @ A_vec, A_vec], dtype=object)  

def rational_approximation(
	Xarr: np.ndarray,
	Yarr: np.ndarray,
	deg: np.int8
) -> np.array:
	"""
	Calculate a vector of values that approximate the corresponding 'Yarr' values
	using a rational function.
	
	Parameters
	----------
	Xarr : np.ndarray
		Vector of x values
	Yarr : np.ndarray
		Vector of y values that corresponds to Xarr; must be the same size as Xarr
	deg : np.int8
		The approximating function's degree, +1
		
	Returns
	-------
	np.ndarray
		A vector of values calculated based on the approximating function."""

	X_vec = np.zeros([Yarr.size, deg])

	for i in np.arange(deg):
		X_vec[:, i] = np.reciprocal(Xarr)**i

	A_vec = np.linalg.inv( np.transpose(X_vec) @ X_vec ) @ np.transpose(X_vec) @ Yarr
	return np.array([X_vec @ A_vec, A_vec], dtype=object)  

def trig_approximation(
	Xarr: np.ndarray,
	Yarr: np.ndarray,
	deg: np.int8,
	constant = np.pi
) -> np.array:
	"""
	Calculate a vector of values that approximate the corresponding 'Yarr' values
	using trig functions.
	
	Parameters
	----------
	Xarr : np.ndarray
		Vector of x values
	Yarr : np.ndarray
		Vector of y values that corresponds to Xarr; must be the same size as Xarr
	deg : np.int8
		The approximating function's degree, +1
	constant: np.float16 = np.pi
		A number that stands before each x in the trig functions; 
		changing it may make the approximating function fit better to the data
		
	Returns
	-------
	np.ndarray
		A vector of values calculated based on the approximating function."""

	X_vec = np.zeros([Yarr.size, deg*2])

	for i in np.arange(deg):
		X_vec[:,2*i]   = np.cos( (constant*i)*Xarr )
		X_vec[:,2*i+1] = np.sin( (constant*i)*Xarr )

	X_vec = np.delete(X_vec, 1, axis = 1)

	A_vec = np.linalg.inv( np.transpose(X_vec) @ X_vec ) @ np.transpose(X_vec) @ Yarr
	return np.array([X_vec @ A_vec, A_vec], dtype=object)  

def av_rel_error(Yarr: np.ndarray, Approxarr: np.ndarray):
	"""
	Calculates the average of absolute values of relative errors between 'Yarr'
	and 'Approxarr'
	
	Parameters
	----------
	Yarr: np.ndarray
		the original dataset
	Approxarr: np.ndarray
		set of data calculated using approximation. 
		The two datasets must be of the same size.
		
	Returns
	-------
	Average relative error between the two datasets"""
	sum = float(0)

	for i, val in np.ndenumerate(Approxarr):
		epsilon = np.abs( (val - Yarr[i]) / val )
		sum = sum + epsilon

	return sum/Yarr.size

def av_abs_error(Yarr: np.ndarray, Approxarr: np.ndarray):
	"""
	Calculates the average of absolute values of absolute errors between 'Yarr'
	and 'Approxarr'
	
	Parameters
	----------
	Yarr: np.ndarray
		the original dataset
	Approxarr: np.ndarray
		set of data calculated using approximation. 
		The two datasets must be of the same size.
		
	Returns
	-------
	Average absolute error between the two datasets"""
	sum = float(0)

	for i, val in np.ndenumerate(Approxarr):
		delta = np.abs( (val - Yarr[i]) )
		sum = sum + delta

	return sum/Yarr.size

def rmse(Yarr: np.ndarray, Approxarr: np.ndarray):
	"""
	Calculates the root mean square error
	
	Parameters
	----------
	Yarr: np.ndarray
		the original dataset
	Approxarr: np.ndarray
		set of data calculated using approximation. 
		The two datasets must be of the same size.
		
	Returns
	-------
	The value of rmse between the two datasets"""
	sum = float(0)

	for i, val in np.ndenumerate(Approxarr):
		sum = sum + np.power( (val - Yarr[i]), 2 )

	return np.sqrt(sum/Yarr.size)

def determination_coeff(Yarr: np.ndarray, Approxarr: np.ndarray):
	"""
	Calculates the determination coefficient
	
	Parameters
	----------
	Yarr: np.ndarray
		the original dataset
	Approxarr: np.ndarray
		set of data calculated using approximation. 
		The two datasets must be of the same size.

	Returns
	-------
	The value of the calculated coefficient of determination between the
	two datasets.
	"""
	upper_sum = float(0)
	lower_sum = float(0)
	yarr_average = stat.arr_average(Yarr)

	for i, val in np.ndenumerate(Yarr):
		upper_sum = upper_sum + (Approxarr[i] - val)**2
		lower_sum = lower_sum + (val - yarr_average)**2

	return 1 - (upper_sum/lower_sum)