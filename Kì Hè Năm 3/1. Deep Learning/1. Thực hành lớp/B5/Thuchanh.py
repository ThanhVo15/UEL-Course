#%% Import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%% modify the charrt's style
plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['font.size'] = 14
plt.rcParams['figure.dpi'] = 150

#%% Prepare the data
# Prepare the data
X = np.array([i for i in range(16)]).reshape(-1, 1)
noise_std_dev = 0.5 # Standard deviation of the noise
# Generate random noise
np.random.seed(40)
noise = np.random.normal(loc=0,scale=noise_std_dev, size=X.shape)
y = X + noise # Create y array by adding noise to X
# Add a column of ones to X to account for the bias term (theta_0)
X_b = np.c_[np.ones((len(X), 1)), X]


plt.scatter(X, y, color='darkblue', s = 80)
plt.xlabel('X', fontweight='bold')
plt.ylabel('y', fontweight='bold')
plt.show()

# Define the cost function
def compute_cost(theta, X, y):
    m = len(y)
    predictions = X.dot(theta)
    cost = (1 / (2 * m)) * np.sum((predictions - y) ** 2)
    return cost

# Define the gradient of the cost function
def compute_gradient(theta, X, y):
    m = len(y)
    predictions = X.dot(theta)
    gradients = (1 / m) * X.T.dot(predictions - y)
    return gradients
    

# Gradient descent algorithm
def gradient_descent(X, y, theta, learning_rate,num_iterations):
    cost_history = []
    theta_history = []
    for i in range(num_iterations):
        gradients = compute_gradient(theta, X, y)
        theta = theta - learning_rate * gradients
        cost = compute_cost(theta, X, y)
        cost_history.append(cost)
        theta_history.append(theta.copy())
    return theta, cost_history, theta_history


#%% Paramters for gradient descent
theta_initial = np.random.randn(2, 1) # Random initialization
learning_rate = 0.01
num_iterations = 500

#%% Perfom gradient descent
theta, cost_history, theta_history = gradient_descent(X_b, y, theta_initial, learning_rate, num_iterations)

#%% Plot the data and the linear regression line
plt.figure(figsize=(14, 7))

plt.subplot(1, 2, 1)
plt.scatter(X, y, color='darkblue', s = 80)
te = X_b.dot(theta)
plt.plot(X, te, color='red', linewidth=2)
plt.xlabel('X', fontweight='bold')
plt.ylabel('y', fontweight='bold')
plt.title('Linear Regression Fit')

# Plot thecost function history
plt.subplot(1, 2, 2)
plt.plot(range(num_iterations), cost_history, color='darkblue', linewidth=2)
plt.xlabel('Iteration', fontweight='bold')
plt.ylabel('Cost', fontweight='bold')
plt.title('Cost Function History')

plt.tight_layout()
plt.show()

#%% Plot the cost function history
plt.scatter(X, y, color='darkblue', s = 80)
plt.plot(X, X_b.dot(theta_history[0]), color='red', linewidth=2, label = 'epoch (0)')
plt.plot(X, X_b.dot(theta_history[1]), color='green', linewidth=2, label = 'epoch (1)')
plt.plot(X, X_b.dot(theta_history[499]), color='orange', linewidth=2, label = 'epoch (end)')
plt.xlabel('X', fontweight='bold')
plt.ylabel('y', fontweight='bold')
plt.legend()
plt.title('Linear Regression Fit')
plt.show()
plt.legend()