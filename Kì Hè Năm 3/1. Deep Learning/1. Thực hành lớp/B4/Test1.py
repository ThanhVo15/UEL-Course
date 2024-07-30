#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [16, 10]
plt.rcParams['figure.dpi'] = 150
plt.rcParams['font.size'] = 15

#%%
def cost_function(theta):
    return np.sin(2 * theta) + np.sin(theta) - 3 

def gradient(theta):
    return 2 * np.cos(2 * theta) + np.cos(theta)

#%%
def gradient_descent(starting_theta, learning_rate, eps, max_iter=10000):
    theta = starting_theta
    theta_history = [theta]
    cost_history = [cost_function(theta)]
    iter_count = 0
    
    while True:
        theta = theta - learning_rate * gradient(theta)
        theta_history.append(theta)
        cost_history.append(cost_function(theta))
        iter_count += 1
        
        if abs(gradient(theta)) < eps or iter_count >= max_iter:
            break
            
    return theta, theta_history, cost_history

#%%
# Khởi tạo các giá trị ban đầu
starting_theta = 0
learning_rate = 0.01
eps = 0.0001

theta, theta_history, cost_history = gradient_descent(starting_theta, learning_rate, eps)

theta_values = np.linspace(-5, 5, 400)
cost_values = cost_function(theta_values)

#%%
plt.figure(figsize=(16, 10))

plt.subplot(1, 2, 1)
plt.plot(theta_values, cost_values, label='$J(\\theta) = \sin(2\\theta) + \sin(\\theta) - 3$', color='darkorange', linewidth=2)
plt.scatter(theta_history, cost_history, color='blue', s=100, label='Gradient Descent')
plt.plot(theta_history, cost_history, color='blue', linewidth=2, linestyle='--')
plt.xlabel('Parameters - $\\theta$')
plt.ylabel('Cost Function - $J(\\theta)$')
plt.title('Cost Function and Gradient Descent Path')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(cost_history, label='Cost Function History', color='darkorange', linewidth=2)
plt.xlabel('Iterations')
plt.ylabel('Cost Function - $J(\\theta)$')
plt.title('Cost Function History')
plt.legend()

plt.tight_layout()
plt.show()

#%%
print(f'The cost function reaches the minimum value of {cost_history[-1]} at theta = {theta_history[-1]}')

