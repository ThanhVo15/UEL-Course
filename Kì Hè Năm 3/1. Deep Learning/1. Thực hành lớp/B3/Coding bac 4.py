#%% import libraries
import numpy as np
import matplotlib.pyplot as plt

#%% Modify the Chart's Appearance
plt.rcParams['figure.figsize'] = [16, 10]
plt.rcParams['figure.dpi'] = 150
plt.rcParams['font.size'] = 15

#%% Define the Cost Function J(theta)= theta^2 -4theta +8
def cost_function(theta):
    return 2*theta**4 - 2*theta**3 - 8*theta**2 +5*theta + 8

#%% Define the derivative of the cost function J'(theta) = 2*theta -4
def gradient(theta):
    return 8*theta**3+ 6*theta**2 + 16 * theta +5

#%% Gradient Descent algorithm
def gradient_descents(starting_theta, learning_rate, eps, max_iter=1500):
    theta = starting_theta
    theta_history = [theta]
    cost_history = [cost_function(theta)]
    iter_count = 0
    while True:
        theta = theta - learning_rate * gradient(theta)
        theta_history.append(theta)
        cost_history.append(cost_function(theta))
        if abs(gradient(theta)) < eps or iter_count > max_iter:
            break
        iter_count += 1
    return theta, theta_history, cost_history

#%% Parameters for gradient descent
starting_theta = 2
learning_rate = 0.001
eps = 0.0001 # stopping threshold

#%% Perform gradient descent
theta, theta_history, cost_history = gradient_descents(starting_theta, learning_rate, eps)

#%% Plot the Cost function
theta_values = np.linspace(-5, 5, 400)
cost_values = cost_function(theta_values)

#%% Plotting the results
plt.figure(figsize=(12, 6))

# Plot the Cost Function and Gradient Descent Path
plt.subplot(1, 2, 1)
theta_values = np.linspace(-2, 2, 400)
cost_values = cost_function(theta_values)
plt.plot(theta_values, cost_values, label='$J(\\theta) = 3\\theta^3 + \\theta^2 - 4\\theta + 8$', color='darkorange', linewidth=2)
plt.scatter(theta_history, cost_history, color='blue', s=100, label='Gradient Descent')
plt.plot(theta_history, cost_history, color='blue', linewidth=2, linestyle='--')
plt.xlabel('Parameters - $\\theta$')
plt.ylabel('Cost Function - $J(\\theta)$')
plt.title('Cost Function and Gradient Descent Path')
plt.legend()

# Plot Cost History
plt.subplot(1, 2, 2)
plt.plot(cost_history, label='Cost Function History', color='darkorange', linewidth=2)
plt.xlabel('Iterations')
plt.ylabel('Cost Function - $J(\\theta)$')
plt.title('Cost Function History')
plt.legend()

plt.tight_layout()
plt.show()


#%% Get results
print(f'The cost function reaches the minimum value of {cost_history[-1]} at theta = {theta_history[-1]}')