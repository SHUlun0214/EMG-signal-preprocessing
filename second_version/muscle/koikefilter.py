import numpy as np
import scipy.signal
import math

def KoikeFilter(emg, sf):
	emg = np.array(emg)
	time = np.arange(0, 1, 1/sf)
	M1 = -10.8*time
	M2 = -16.52*time
	# print(emg.shape)
	"""
	coef
	"""
	coef = []
	for i in range(sf):
		M1[i] = math.exp(M1[i])
		M2[i] = math.exp(M2[i])
		coef.append(6.44 * (M1[i] - M2[i]))

	"""
	total
	"""
	total = sum(coef)


	"""
	zf
	"""
	zi = scipy.signal.lfilter_zi(coef, 1)
	zf = np.ones([sf-1, 32])
	for i in range(sf-1):
		for j in range(emg.shape[0]):
			zf[i,j] = zf[i,j] * zi[i]

	emg = emg.T
	y = np.zeros([emg.shape[0], emg.shape[1]])
	for i in range(y.shape[1]):
		xn = np.abs(emg[:,i]/total)
		y[:,i], zf[:,i] = scipy.signal.lfilter(coef, 1.0, xn, axis=-1, zi=zf[:,i])

	return y, zf
