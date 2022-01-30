import numpy as np
from sklearn.metrics import mean_squared_error

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()
    
z = [1.0, 2.0, 3.0, 4.0, 1.0, 2.0] #[0.02864414 0.07786284 0.21165314 0.5753329  0.02864414 0.07786284]

print(softmax(z))
print(np.argmax(z)) #vervangen met zelf gemaakte functie

print(mean_squared_error(z))