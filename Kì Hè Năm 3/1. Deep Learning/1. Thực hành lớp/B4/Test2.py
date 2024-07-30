#%% 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#%%
data = pd.read_xml(r'D:\GitHub\UEL-Course\Kì Hè Năm 3\1. Deep Learning\1. Thực hành lớp\B4\data.xml')
print(data.head())
#%% Preprocessing
# Check null
print("-"*20)
x = data.isnull().sum()
print(f'So luong null {x}')
print("-"*20)
y = data.duplicated().sum()
print(f'So luong ban ghi trung lap: {y}')
print("-"*20)
if y > 0:
    data = data.drop_duplicates()
    print(f'Số lượng bản ghi sau khi loại bỏ trùng lặp: {len(data)}')
#%% Label
print("-"*20)
label_color = data['Color'].unique()
print(f'Cac gia tri trong Color: {label_color}')
label_category = data['Category'].unique()
print("-"*20)
print(f'Cac gia tri trong category: {label_category}')
print("-"*20)

# Encoding
def one_hot_encode(df, column):
    return pd.get_dummies(df[column], prefix=column)

color_encoded = one_hot_encode(data, 'Color')
category_encoded = one_hot_encode(data, 'Category')

data_encoded = pd.concat([data.drop(['Color', 'Category'], axis=1), color_encoded, category_encoded], axis=1)

# Split features and labels
X = data_encoded.drop(columns=category_encoded.columns)
y = category_encoded.values

# Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Initialize parameters
def initialize_parameters(input_size, hidden_size, output_size):
    W1 = np.random.randn(input_size, hidden_size) * 0.01
    b1 = np.zeros((1, hidden_size))
    W2 = np.random.randn(hidden_size, output_size) * 0.01
    b2 = np.zeros((1, output_size))
    return W1, b1, W2, b2

# Activation functions
def relu(Z):
    return np.maximum(0, Z)

def softmax(Z):
    exp_Z = np.exp(Z - np.max(Z))
    return exp_Z / exp_Z.sum(axis=1, keepdims=True)

# Forward propagation
def forward_propagation(X, W1, b1, W2, b2):
    Z1 = np.dot(X, W1) + b1
    A1 = relu(Z1)
    Z2 = np.dot(A1, W2) + b2
    A2 = softmax(Z2)
    cache = (Z1, A1, Z2, A2)
    return A2, cache

# Compute loss
def compute_loss(Y, A2):
    m = Y.shape[0]
    log_probs = np.multiply(np.log(A2), Y)
    loss = -np.sum(log_probs) / m
    return loss

# Backward propagation
def backward_propagation(X, Y, cache, W1, W2):
    m = X.shape[0]
    Z1, A1, Z2, A2 = cache

    dZ2 = A2 - Y
    dW2 = np.dot(A1.T, dZ2) / m
    db2 = np.sum(dZ2, axis=0, keepdims=True) / m

    dA1 = np.dot(dZ2, W2.T)
    dZ1 = dA1 * (Z1 > 0)
    dW1 = np.dot(X.T, dZ1) / m
    db1 = np.sum(dZ1, axis=0, keepdims=True) / m

    return dW1, db1, dW2, db2

# Update parameters
def update_parameters(W1, b1, W2, b2, dW1, db1, dW2, db2, learning_rate):
    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2
    return W1, b1, W2, b2

# Train model
def train(X, Y, input_size, hidden_size, output_size, learning_rate=0.01, epochs=10000):
    W1, b1, W2, b2 = initialize_parameters(input_size, hidden_size, output_size)
    loss_history = []
    accuracy_history = []

    for epoch in range(epochs):
        A2, cache = forward_propagation(X, W1, b1, W2, b2)
        loss = compute_loss(Y, A2)
        loss_history.append(loss)
        
        y_pred = np.argmax(A2, axis=1)
        y_true = np.argmax(Y, axis=1)
        accuracy = np.mean(y_pred == y_true)
        accuracy_history.append(accuracy)

        dW1, db1, dW2, db2 = backward_propagation(X, Y, cache, W1, W2)
        W1, b1, W2, b2 = update_parameters(W1, b1, W2, b2, dW1, db1, dW2, db2, learning_rate)

        if epoch % 100 == 0:
            print(f'Epoch {epoch}, loss: {loss}, accuracy: {accuracy}')

    return W1, b1, W2, b2, loss_history, accuracy_history


# Predict
def predict(X, W1, b1, W2, b2):
    A2, _ = forward_propagation(X, W1, b1, W2, b2)
    return np.argmax(A2, axis=1)

# Train the model
input_size = X_train.shape[1]
hidden_size = 64
output_size = y_train.shape[1]
learning_rate = 0.01
epochs = 10000

W1, b1, W2, b2, loss_history, accuracy_history = train(X_train, y_train, input_size, hidden_size, output_size, learning_rate, epochs)

# Evaluate the model
y_pred = predict(X_test, W1, b1, W2, b2)
y_test_labels = np.argmax(y_test, axis=1)

accuracy = np.mean(y_pred == y_test_labels)
print(f'Accuracy: {accuracy}')

# Plotting results
plt.figure(figsize=(16, 6))

plt.subplot(1, 3, 1)
plt.plot(loss_history, label='Training Loss', color='darkorange', linewidth=2)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Loss History')
plt.legend()

plt.subplot(1, 3, 2)
plt.scatter(range(len(y_test_labels)), y_test_labels, label='True Labels', color='blue', s=100)
plt.scatter(range(len(y_pred)), y_pred, label='Predicted Labels', color='red', s=100, marker='x')
plt.xlabel('Sample Index')
plt.ylabel('Category')
plt.title('True vs Predicted Labels')
plt.legend()

plt.subplot(1, 3, 3)
plt.plot(accuracy_history, label='Training Accuracy', color='blue', linewidth=2)
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Training Accuracy History')
plt.legend()

plt.tight_layout()
plt.show()

