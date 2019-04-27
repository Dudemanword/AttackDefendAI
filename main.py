from GenerateTrainingData import GenerateTrainingData
from GenerateTestData import GenerateTestData
from typing import List,Tuple
from actions import Action
from result import Result

import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

trainingData: List[Tuple[Action, Action, Result]] = GenerateTrainingData()
trainingPlayerActions = []
trainingEnemyResponse = []
trainingResults = []

testPlayerActions = []
testEnemyResponse = []
testResults = []

for res in trainingData:
    trainingPlayerActions.append(res[0].value)
    trainingEnemyResponse.append(res[1].value)
    trainingResults.append(res[2].value)

testData:List[Tuple[Action, Action, Result]] = GenerateTestData(60000)
for res in testData:
    testPlayerActions.append(res[0].value)
    testEnemyResponse.append(res[1].value)
    testResults.append(res[2].value)

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(100, 100)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])
model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
              
model.fit(np.array(trainingPlayerActions), np.array(trainingResults), epochs=5)
test_loss, test_acc = model.evaluate(np.array(testPlayerActions), np.array(testResults))
print('Test accuracy:', test_acc)

