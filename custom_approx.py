import numpy as np

def polynomial_approximation(
	Xarr: np.ndarray, 
	Yarr: np.ndarray,
	deg: np.int8
) -> np.ndarray:
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
	X_vec = np.zeros([Yarr.size, deg])

	for i in np.arange(deg):
		X_vec[:, i] = np.log(Xarr)**i

	A_vec = np.linalg.inv( np.transpose(X_vec) @ X_vec ) @ np.transpose(X_vec) @ Yarr
	return (X_vec @ A_vec)