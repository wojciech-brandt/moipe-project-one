from os import path
import config as cfg
import numpy as np
import custom_statistics as stat
import custom_approx as approx

	
def main():
	# importing the data files if they exist, creating them if not
	if not path.isfile(cfg.preliminary['FILE_NAME']):
		import subprocess

		U = np.zeros(cfg.preliminary['REPETITIONS'])

		for i in np.arange(cfg.preliminary['REPETITIONS']):
			program_output = subprocess.run(
				[cfg.executable['EXE_NAME'], str(cfg.preliminary['EXAMINED_POINT'])],
				capture_output=True, text=True
			)
			U[i] = program_output.stdout

		X = np.ones(cfg.preliminary['REPETITIONS'])*cfg.preliminary['EXAMINED_POINT']
		out = np.stack([X, U])
		np.savetxt(cfg.preliminary['FILE_NAME'], out, delimiter=",")

	if not path.isfile(cfg.main['FILE_NAME']):
		import subprocess

		X = np.linspace(
			cfg.main['START_POINT'],
			cfg.main['END_POINT'],
			cfg.main['NO_POINTS']
		)
		U = np.zeros(cfg.main['NO_POINTS'])

		for i, val in np.ndenumerate(X):
			program_output = subprocess.run(
				[cfg.executable['EXE_NAME'], str(val)],
				capture_output=True, text=True
			)
			U[i] = program_output.stdout

		out = np.stack([X, U])
		np.savetxt(cfg.main['FILE_NAME'], out, delimiter=",")

	

if __name__ == '__main__':
	main()