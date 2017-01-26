# Machine Learning Online Class - Exercise 1: Linear Regression

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from warm_up_exercise import warm_up_exercise
from plot_data import plot_data
from compute_cost import compute_cost
from gradient_descent import gradient_descent


# ==================== Part 1: Basic Function ====================
print 'Running warmUpExercise...'
print '5x5 Identity Matrix: '

print warm_up_exercise()

# raw_input("Program paused. Press enter to continue.")


# ======================= Part 2: Plotting =======================
print "Plotting Data..."

data = np.loadtxt(open("ex1data1.txt", "r"), delimiter=",")
x = data[:, 0:1]
y = data[:, 1:2]
m = len(y)  # Number of training examples

# Plot data
plot_data(x, y)

# raw_input("Program paused. Press enter to continue.")


# =================== Part 3: Gradient descent ===================
print 'Running Gradient Descent...'

x = np.concatenate((np.ones((m, 1)), x), axis=1)  # Add a column of ones to x
theta = np.zeros((2, 1))  # Initialize fitting parameters

# Some gradient descent settings
iterations = 1500
alpha = 0.01

# Compute and display initial cost
cost = compute_cost(x, y, theta)
print cost

# Run gradient descent
[theta, j_history] = gradient_descent(x, y, theta, alpha, iterations)

# Print theta to screen
print "Theta found by gradient descent:", theta

plt.plot(x[:, 1], np.dot(x, theta), label='Linear Regression')
plt.legend(loc='upper left', numpoints=1)

# Predict values for population sizes of 35,000 and 70,000
predict1 = np.dot(np.array([1, 3.5]), theta)
print "For population = 35,000, we predict a profit of", predict1 * 10000
predict2 = np.dot(np.array([1, 7]), theta)
print "For population = 70,000, we predict a profit of", predict2 * 10000

# raw_input("Program paused. Press enter to continue.")


# ============= Part 4: Visualizing J(theta_0, theta_1) =============
print "Visualizing J(theta_0, theta_1) ..."

# Grid over which we will calculate J
theta0_vals = np.linspace(-10, 10, 100)
theta1_vals = np.linspace(-1, 4, 100)

j_vals = np.zeros((len(theta0_vals), len(theta1_vals)))

# Fill out j_vals
for i in range(len(theta0_vals)):
    for j in range(len(theta1_vals)):
        t = np.array([[theta0_vals[i], theta1_vals[j]]]).T
        j_vals[i, j] = compute_cost(x, y, t)

# We need to transpose J_vals before calling plot_surface, or else the axes will be flipped.
j_vals = j_vals.T
theta0_vals, theta1_vals = np.meshgrid(theta0_vals, theta1_vals)

# Surface plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(theta0_vals, theta1_vals, j_vals, rstride=2, cstride=2, cmap=cm.jet, linewidth=0, antialiased=False)
ax.set_xlabel(r'$\theta_0$')
ax.set_ylabel(r'$\theta_1$')

# Contour plot
plt.figure()
# Plot J_vals as 15 contours spaced logarithmically between 0.01 and 100
plt.contour(theta0_vals, theta1_vals, j_vals, levels=np.logspace(-2, 3, 20))
plt.plot(theta[0], theta[1], linestyle='', marker='x', color='r')
plt.xlabel(r'$\theta_0$')
plt.ylabel(r'$\theta_1$')

plt.show()
