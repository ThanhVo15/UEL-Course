import numpy as np
from sklearn.preprocessing import StandardScaler, RobustScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt

#%% Modify the chart's appearance
plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['font.size'] = 14
plt.rcParams['figure.dpi'] = 150

#%% Data Preprocessing

# Input Dataset (weight, Size)
inputs = np.array([[120,10], [180,12], [90,8], [110,7.5], [150,11], [170,13], [95,9], [130,10.5], [200,14], [100,8]])

# Labels (One Hot Encoded): Eggplant = 1, Carrot = 0
outputs = np.array([[1], [1], [0], [0], [1], [1], [0], [1], [1], [0]])

# Normalize the inputs
# scaler = StandardScaler()
# inputs_scaled = scaler.fit_transform(inputs)

scaler = RobustScaler()
inputs_scaled = scaler.fit_transform(inputs)


# inputs_scaled = inputs/np.max(inputs, axis=0)

#%% Training Hyper Parameters
epochs = 1000
learning_rate = 0.1

#%% Define the Model Architecture
class SimpleNeuralNetwork:

    def __init__(self, input_size, hidden_size, output_size):
        self.weights_hidden_input = np.random.randn(input_size, hidden_size)
        self.bias_hidden = np.zeros((1, hidden_size))
        self.weights_hidden_output = np.random.randn(hidden_size, output_size)
        self.bias_output = np.zeros((1, output_size))

    @staticmethod
    def sigmoid(x):
        return 1/(1+np.exp(-x))
        
    @staticmethod
    def sigmoid_derivative(x):
        return x*(1-x)
        
    def forward(self, X):
        self.hidden_layer_values = np.dot(X, self.weights_hidden_input) + self.bias_hidden
        self.hidden_layer_output = self.sigmoid(self.hidden_layer_values)
        self.output_layer_values = np.dot(self.hidden_layer_output, self.weights_hidden_output) + self.bias_output
        self.output_layer_out = self.sigmoid(self.output_layer_values)
        return self.output_layer_out
        
    def backward(self,X, y, predicted):
        dS_out = predicted - y
        dW_out = np.dot(self.hidden_layer_output.T, dS_out)
        db_out =  np.sum(dS_out, axis = 0 , keepdims= True)

        dS_hidden = np.dot(dS_out, self.weights_hidden_output.T) * self.sigmoid_derivative(self.hidden_layer_output)
        dW_hidden = np.dot(X.T, dS_hidden)
        db_hidden = np.sum(dS_hidden, axis = 0, keepdims = True)

        return dW_hidden, db_hidden, dW_out, db_out
        
    def update(self, dW_hidden, db_hidden, dW_out, db_out):
        self.weights_hidden_input -= learning_rate * dW_hidden
        self.bias_hidden -= learning_rate * db_hidden
        self.weights_hidden_output -= learning_rate * dW_out
        self.bias_output -= learning_rate * db_out

    def predict(self,X):
        return self.forward(X)
        
#%% Initialize the Model
model = SimpleNeuralNetwork(inputs_scaled.shape[1], 2, outputs.shape[1])

#%% Training Loop
cost_history = []
tolerance = 1e-6  # Giá trị nhỏ nhất để xem xét sự thay đổi của hàm lỗi
epochs = 0
max_epochs = 10000  # Số lượng epochs tối đa để tránh lặp vô hạn

while True:
    # Forward Pass
    predicted = model.forward(inputs_scaled)
    # Calculate Loss (binary cross-entropy)
    cost = -np.mean(np.sum(outputs * np.log(predicted) + (1 - outputs) * np.log(1 - predicted), axis=1))
    cost_history.append(cost)

    # Check if the improvement in cost is smaller than the tolerance
    if epochs > 0 and (cost_history[-2] - cost) < tolerance:
        print(f'Training stopped: Cost at epoch {epochs}: {cost}')
        break

    # Backward pass and update weights
    dW1, db1, dW2, db2 = model.backward(inputs_scaled, outputs, predicted)
    model.update(dW1, db1, dW2, db2)

    # Print loss for each epoch
    if epochs % 100 == 0:
        print(f'Cost at epoch {epochs}: {cost}')

    epochs += 1
    if epochs >= max_epochs:
        print("Reached maximum epochs limit.")
        break

#%% Final Output after training
predicted_output = model.predict(inputs_scaled)
print("Predicted Output: ", predicted_output)

#%% Plotting the Cost over epochs
plt.plot(cost_history, lw = 3, color = 'darkblue')
plt.xlabel('Epochs', fontweight='bold')
plt.ylabel('Cost', fontweight='bold')
plt.title('Cost vs Epochs', fontweight='bold')
plt.show()

#%% Evaluate the model
# Predicted Probabilities
predicted_probs = predicted_output.reshape(-1)

# Actual labels
real_values = outputs
# Convert predicted probabilities to binary predictiosn using a threshold of 0.8
predicted_labels = (predicted_probs > 0.8).astype(int)

# Calculate the evaluation metrics
accuracy = accuracy_score(real_values, predicted_labels)
precision = precision_score(real_values, predicted_labels)
recall = recall_score(real_values, predicted_labels)
f1 = f1_score(real_values, predicted_labels)

# Print the results
print('Accuracy:', accuracy)
print('Precision:', precision)
print('Recall:', recall)
print('F1 Score:', f1)


