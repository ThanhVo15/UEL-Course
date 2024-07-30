#%% import libraries
import numpy as np
import matplotlib.pyplot as plt

#%% Modify the Chart's Appearance
plt.rcParams['figure.figsize'] = [10, 8]
plt.rcParams['figure.dpi'] = 150
plt.rcParams['font.size'] = 15

#%% Define the Cost Function J(theta)= theta^2 -4theta +8
def cost_function(theta):
    return theta**2 - 4 * theta + 8

#%% Define the derivative of the cost function J'(theta) = 2*theta -4
def gradient(theta):
    return 2 * theta - 4

#%% Gradient Descent algorithm
def gradient_descents(starting_theta, learning_rate, eps):
    theta = starting_theta
    theta_history = [theta]
    cost_history = [cost_function(theta)]
    while True:
        theta = theta - learning_rate * gradient(theta)
        theta_history.append(theta)
        cost_history.append(cost_function(theta))
        if abs(gradient(theta)) < eps:
            break

    return theta, theta_history, cost_history

#%% Parameters for gradient descent
starting_theta = 5
learning_rate = 0.1
eps = 0.0001 # stopping threshold

#%% Perform gradient descent
theta, theta_history, cost_history = gradient_descents(starting_theta, learning_rate, eps)

#%% Plot the Cost function
theta_values = np.linspace(-1, 5, 400)
cost_values = cost_function(theta_values)

plt.figure(figsize=(12, 6))

# Plot the Cost Function
plt.subplot(1, 2, 1)
plt.plot(theta_values, cost_values, label='$J(\\theta) = \\theta^2 - 4\\theta + 8$', color='darkorange', linewidth=2)
plt.scatter(theta_history, cost_history, color='blue', s=100, label='Gradient Descent')
plt.plot(theta_history, cost_history, color='blue', linewidth=2, linestyle='--')
plt.xlabel('Parameters - $\\theta$')
plt.ylabel('Cost Function - $J(\\theta)$')
plt.title('Cost Function and Gradient Descent Path')
plt.legend()

# Plot Cost History
plt.subplot(1, 2, 2)
plt.plot(cost_history, label='Cost Function', color='darkorange', linewidth=2)
plt.xlabel('Iterations')
plt.ylabel('Cost Function - $J(\\theta)$')
plt.title('Cost Function History')
plt.legend()

plt.tight_layout()
plt.show()

#%% Get results
print(f'The cost function reaches the minimum value of {cost_history[-1]} at theta = {theta_history[-1]}')
