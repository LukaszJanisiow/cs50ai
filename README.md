I started with the same layers as in the lecture in the handwriting.py:
- 2D convolutional layer of 32 filters
- max-Pooling layer with a pool size of 2x2
- flattening layer
- dense hidden layer of 128 neurons
- dropout layer with a rate of 50%
Result accuracy: 5,53 %

Next try (remove hidden layer):
- 2D convolutional layer of 32 filters
- max-Pooling layer with a pool size of 2x2
- flattening layer
Result accuracy: 92,88 %

Next try (add second convolutional and max-pooling layer):
- 2D convolutional layer of 32 filters
- max-Pooling layer with a pool size of 2x2
- 2D convolutional layer of 64 filters
- max-Pooling layer with a pool size of 2x2
- flattening layer
Result accuracy: 93,29 %

Next try (add hidden layer of 128 neurons with dropout 50%):
- 2D convolutional layer of 32 filters
- max-Pooling layer with a pool size of 2x2
- 2D convolutional layer of 64 filters
- max-Pooling layer with a pool size of 2x2
- flattening layer
- dense hidden layer of 128 neurons
- dropout layer with a rate of 50%
Result accuracy: 95,93 %

Next try (change hidden layer to 256 neurons):
- 2D convolutional layer of 32 filters
- max-Pooling layer with a pool size of 2x2
- 2D convolutional layer of 64 filters
- max-Pooling layer with a pool size of 2x2
- flattening layer
- dense hidden layer of 128 neurons
- dropout layer with a rate of 50%
Result accuracy: 96,73 %