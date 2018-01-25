from statistics import mean
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

style.use('fivethirtyeight')


file1 = open("time3.csv", "r")
#print()
a = []
b = []
c = file1.readline()
c = file1.readline()
c = c.strip()
while(c):
	c = c.split(",")
	#print(c)
	a.append(int(c[0]))
	b.append(float(c[1]))
	c = file1.readline()
	c = c.strip()

#a = [1,2,3,4,5,6]
#b = [5,4,6,5,6,7]
xs = np.array(a, dtype = np.float64)
ys = np.array(b, dtype = np.float64)

def best_fit_slope_and_intercept(xs,ys):
	m = (mean(xs) * mean(ys) - mean(xs*ys)) / (mean(xs)*mean(xs) - mean(xs*xs))
	b = (mean(ys) - m * mean(xs))
	return m, b

def squared_error(ys_orig, ys_line):
	return sum((ys_line - ys_orig)**2)

def coefficient_of_determination(ys_orig, ys_line):
	y_mean_line = [mean(ys_orig) for y in ys_orig]
	squared_error_regr = squared_error(ys_orig, ys_line)
	squared_error_y_mean = squared_error(ys_orig, y_mean_line)
	return 1 - (squared_error_regr / squared_error_y_mean)



m, b = best_fit_slope_and_intercept(xs,ys)
#print(m)
#print(b)
 
regression_line = [((m*x) + b) for x in xs]
#print(regression_line) 

r_squared = coefficient_of_determination(ys, regression_line)	#r_squared
#print(r_squared)


predict_x = 4
predict_y = (m*predict_x) + b

plt.scatter(xs,ys)
plt.scatter(predict_x, predict_y, color = 'r')
plt.plot(xs, regression_line)
plt.show()
