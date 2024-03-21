import matplotlib.pyplot as plt
import scipy.interpolate 
import numpy as np

plt.figure(figsize=(6,6))

bottomx = np.array([0, 0.01, 0.028, 0.058, 0.147, 0.196, 0.326, 0.427, 0.837,1])
bottomy = np.array([0, -0.01, -0.017, -0.023, -0.033, -0.038, -0.044, -0.043, -0.013, 0])


x = np.array([0, 0.022, 0.031, 0.062, 0.155, 0.201, 0.33, 0.53, 0.681, 1])
y = np.array([0, 0.034, 0.04, 0.053, 0.071, 0.075, 0.077, 0.063, 0.047, 0])

x_fit = np.linspace(min(x), max(x), 1000)
y_up = scipy.interpolate.interp1d(x, y, kind='cubic')
y_down = scipy.interpolate.interp1d(bottomx, bottomy, kind='cubic')

cp_top = np.array([0, 3.5, 3.25, 3.19, 1.56, 1.38, 1, 0.63, 0.44, 0.06])
cp_bottom = np.array([0, -1, -0.88, -0.63, -0.38, -0.25, -0.06, -0, 0.06, 0.06])
plt.plot(x_fit, y_up(x_fit), label='Cubic Fit Curve', color='grey')
plt.plot(x_fit, y_down(x_fit), label='Cubic Fit Curve', color='grey')

c_top = scipy.interpolate.interp1d(x, cp_top, kind='cubic')
c_bottom = scipy.interpolate.interp1d(bottomx, cp_bottom, kind='cubic')

plt.scatter(x, cp_top, )
plt.scatter(bottomx, cp_bottom)
plt.plot(x_fit, c_top(x_fit), label='Cubic Fit Curve', color='black')
plt.plot(x_fit, c_bottom(x_fit), label='Cubic Fit Curve', color='black')

plt.axis((-0.5, 1.5, -1.5, 4))


plt.show()


