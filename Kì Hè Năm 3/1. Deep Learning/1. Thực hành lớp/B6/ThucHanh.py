#%% Import Library
import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping

#%% Modify the chart's appearance
plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['font.size'] = 14
plt.rcParams['figure.dpi'] = 150

#%% Prepare the data
X = np.array([i for i in range(16)]).reshape(-1, 1)
noise_std_dev = 0.5 # Standard deviation of the noise
# Generate random noise
noise = np.random.normal(loc=0, scale=noise_std_dev, size=X.shape)
y = X + noise # Create y array by adding noise to X

# Add a column of ones to X to account for the bias term (theta_0)
X_b = np.c_[np.ones((len(X), 1)), X]
print(X_b.shape[1])

#%% Plotting Data
plt.scatter(X, y, color='darkblue', s=80)
plt.xlabel('X', fontweight='bold')
plt.ylabel('y', fontweight='bold')
plt.show()

#%% Define the model
model = Sequential()
model.add(keras.Input(shape=(X_b.shape[1],))) # Input shape based on X_b columns
model.add(Dense(10, activation='relu')) 
model.add(Dense(10, activation='relu'))
model.add(Dense(1))

#%% Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

#%% Train the model
# Define the early stopping callback
early_stopping = EarlyStopping(monitor='loss', min_delta=0.001, patience=10, restore_best_weights=True)

#%% Train the model with Early Stopping
history = model.fit(X_b, y, epochs=2000, callbacks=[early_stopping])

#%% Plot the training and validation loss
plt.plot(history.history['loss'], label='Training Loss', color='darkblue', lw=3)
plt.xlabel('Epoch', fontweight='bold')
plt.ylabel('Loss', fontweight='bold')
plt.legend()
plt.show()

#%% Evaluate the model
loss = model.evaluate(X_b, y)
print('Loss:', loss)

#%% Make Predictions
y_pred = model.predict(X_b)

#%% Plot the data and the model's predictions
plt.scatter(X, y, color='darkblue', s=80, label='Data')
plt.plot(X, y_pred, color='red', lw=3, label='Predictions')
plt.xlabel('X', fontweight='bold')
plt.ylabel('y', fontweight='bold')
plt.legend()
plt.show()

#%% Make predictions for new data
new_X = np.array([i for i in range(20, 26)])
new_X_b = np.c_[np.ones((len(new_X), 1)), new_X]
print(model.predict(new_X_b))


