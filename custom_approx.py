import numpy as np

def polynomial_approximation(
	Xarr: np.ndarray, 
	Yarr: np.ndarray,
	deg: np.int8
) -> np.ndarray:
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
	assert (Xarr.size == Yarr.size), "Xarr and Yarr must be the same size."
	
	X_vec = np.zeros([Yarr.size, deg])

	for i in np.arange(deg):
		X_vec[:, i] = Xarr**i

	A_vec = np.linalg.inv( np.transpose(X_vec) @ X_vec ) @ np.transpose(X_vec) @ Yarr
	return (X_vec @ A_vec)

def natlog_approximation(
	Xarr: np.ndarray,
	Yarr: np.ndarray,
	deg: np.int8
) -> np.ndarray:
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
	assert (Xarr.size == Yarr.size), "Xarr and Yarr must be the same size."

	X_vec = np.zeros([Yarr.size, deg])

	for i in np.arange(deg):
		X_vec[:, i] = np.log(Xarr)**i

	A_vec = np.linalg.inv( np.transpose(X_vec) @ X_vec ) @ np.transpose(X_vec) @ Yarr
	return (X_vec @ A_vec)

def rational_approximation(
	Xarr: np.ndarray,
	Yarr: np.ndarray,
	deg: np.int8
) -> np.ndarray:
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
	assert (Xarr.size == Yarr.size), "Xarr and Yarr must be the same size."

	X_vec = np.zeros([Yarr.size, deg])

	for i in np.arange(deg):
		X_vec[:, i] = np.reciprocal(Xarr)**i

	A_vec = np.linalg.inv( np.transpose(X_vec) @ X_vec ) @ np.transpose(X_vec) @ Yarr
	return (X_vec @ A_vec)

def trig_approximation(
	Xarr: np.ndarray,
	Yarr: np.ndarray,
	deg: np.int8,
	constant: np.float16 = np.pi
) -> np.ndarray:
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
	assert (Xarr.size == Yarr.size), "Xarr and Yarr must be the same size."

	X_vec = np.zeros([Yarr.size, deg*2])

	for i in np.arange(deg):
		X_vec[:,2*i] = np.cos(constant*i*Xarr)
		X_vec[:,2*i+1] = np.sin(constant*i*Xarr)

	X_vec = np.delete(X_vec, 1, axis = 1)

	A_vec = np.linalg.inv( np.transpose(X_vec) @ X_vec ) @ np.transpose(X_vec) @ Yarr
	return (X_vec @ A_vec)

