import matplotlib.pyplot as plt
import numpy as np

# Model complexity (x-axis)
complexity = np.linspace(1, 10, 100)

# Accuracy curves
train_accuracy = np.tanh(complexity)  # training accuracy increases with complexity
test_accuracy = np.tanh(complexity) - 0.1*(complexity-5)**2/25  # test accuracy drops if too complex

plt.figure(figsize=(10,6))
plt.plot(complexity, train_accuracy, label="Training Accuracy", color='blue', linewidth=2)
plt.plot(complexity, test_accuracy, label="Test Accuracy", color='red', linewidth=2)

# Highlight areas
plt.axvspan(0, 3, color='yellow', alpha=0.2, label='Underfitting')
plt.axvspan(3, 7, color='green', alpha=0.2, label='Good Fit')
plt.axvspan(7, 10, color='orange', alpha=0.2, label='Overfitting')

plt.xlabel("Model Complexity")
plt.ylabel("Accuracy")
plt.title("Underfitting vs Good Fit vs Overfitting")
plt.legend()
plt.grid(True)
plt.show()
