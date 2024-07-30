import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import keras

# Data Preprocessing
inputs = np.array([[120, 10], [180, 12], [90, 8], [110, 7.5], [150, 11], [170, 13], [95, 9], [130, 10.5], [200, 14], [100, 8]])
outputs = np.array([[1], [0], [1], [0], [1], [0], [1], [0], [1], [0]])

# Normalize the inputs
scaler = StandardScaler()
inputs_scaled = scaler.fit_transform(inputs)

# Define the model
model = Sequential([
    Dense(2, activation='softmax', input_shape=(inputs_scaled.shape[1],)),
    Dense(2, activation='softmax'),
    Dense(1, activation='softmax')
])

# Compile the model
model.compile(optimizer=keras.optimizers.SGD(learning_rate=0.1),
loss=keras.losses.BinaryCrossentropy(), metrics=['accuracy'])

# Training the model
history = model.fit(inputs_scaled, outputs, epochs=1000, batch_size=10, verbose=2)

# Plotting the training progress
plt.plot(history.history['loss'], label='Loss', color='darkorange')
plt.title('Cost over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Cost')
plt.legend()
plt.show()

# Predicting the outputs
predicted_output = model.predict(inputs_scaled)
print("Predicted outputs after training:")
print(predicted_output)
