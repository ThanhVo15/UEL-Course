## Coding the Sigmoid Activation Function

#%% Import Libraries
import numpy as np
import matplotlib.pyplot as plt

#%% Modify the chart function
plt.rcParams['figure.figsize'] = [10, 8]
plt.rcParams['figure.dpi'] = 200
plt.rcParams['font.size'] = 12

#%% Define the sigmoid function

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#%% Generate an array of value from -10 to 10
x = np.linspace(-10,10,400)
y = sigmoid(x)

#%% plot the sigmoid function
def plot_sigmoid_function(x,y):
    plt.plot(x, y, label= 'Sigmoid Function', color = 'darkorange', linewidth = 6)
    plt.xlabel('Input')
    plt.ylabel('Output')
    plt.title('Sigmoid Function', fontweight = 'bold')
    plt.legend()
    plt.grid(True)
    plt.show()

#plot_sigmoid_function(x,y)



## Coding the Tanh Activation Function

#%%% Define the tanh funtion
def tanh(x):
    return np.tanh(x)

#%% Generate an array of value from -10 to 10
x_tanh = np.linspace(-10,10,400)
y_tanh = tanh(x_tanh)

#%% Plot the Tanh Function
def plot_tanh_function(x_tanh,y_tanh):
    plt.plot(x_tanh,y_tanh, label = 'Tanh Function', color = 'darkorange', linewidth = 8 )
    plt.title('Tanh Function', fontweight = 'bold')
    plt.xlabel('Input')
    plt.ylabel('Output')
    plt.axhline(y=0, color = 'black', linewidth = 1, linestyle = '-')
    plt.legend()
    plt.grid(True)
    plt.show()

# plot_tanh_function(x_tanh, y_tanh)

#--------------------------------------------------------------
## Coding the ReLU Activation Function
#%% Define the ReLU function
def ReLU(x):
    return np.maximum(0,x)

#%% Generate an array of value from -10 to 10
x_relu = np.linspace(-10,10,400)
y_relu = ReLU(x_relu)

#%% Plot the ReLU Function
def plot_ReLU_function(x_relu, y_relu):
    plt.plot(x_relu, y_relu, label = 'ReLU Function', color = 'darkorange', linewidth = 6)
    plt.title('ReLU Function', fontweight = 'bold')
    plt.xlabel('Input')
    plt.ylabel('Output')
    plt.legend()
    plt.grid(True)
    plt.show()

# plot_ReLU_function(x_relu, y_relu)

#--------------------------------------------------------------
#%% Coding the Leaky ReLU Activation Function
def leaky_relu_function(x, alpha = 0.01):
    return np.maximum(alpha*x, x)

#%% Generate an array of value from -10 to 10
x_leaky_relu = np.linspace(-10,10,400)
y_leaky_relu = leaky_relu_function(x_leaky_relu)

#%% Plot the Leaky ReLU Function
def plot_leaky_relu_function(x_leaky_relu, y_leaky_relu):
    plt.plot(x_leaky_relu, y_leaky_relu, label = 'Leaky ReLU Function', color = 'darkorange', linewidth = 6)
    plt.title('Leaky ReLU Function', fontweight = 'bold')
    plt.xlabel('Input')
    plt.ylabel('Output')
    plt.legend()
    plt.grid(True)
    plt.show()

plot_leaky_relu_function(x_leaky_relu, y_leaky_relu)

#--------------------------------------------------------------
#%% Coding the Softmax Activation Function
def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis = 0)

#%% Generate an array of value from -10 to 10
x_softmax = np.linspace(-10,10,400)
y_softmax = softmax(x_softmax)

#%% Plot the Softmax Function
def plot_softmax_function(x_softmax, y_softmax):
    plt.plot(x_softmax, y_softmax, label = 'Softmax Function', color = 'darkorange', linewidth = 6)
    plt.title('Softmax Function', fontweight = 'bold')
    plt.xlabel('Input')
    plt.ylabel('Output')
    plt.legend()
    plt.grid(True)
    plt.show()

plot_softmax_function(x_softmax, y_softmax)
